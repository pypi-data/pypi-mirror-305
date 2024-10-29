# Receives the Semantic Data extracted by the AGParser and generates the Interpreter class needed to calculate de attributes

from lark.visitors import Interpreter
import re
import warnings


def __find_nth_occurrence__(lst, element, n):
    indices = [index for index, value in enumerate(lst) if value == element]
    if n <= len(indices):
        return indices[n - 1]
    else:
        return -1  # Return -1 if nth occurrence doesn't exist
    
def topological_sort(dependencies):
    # Initialize variables
    graph = {}
    visited = set()
    order = []

    # Build graph
    for key, deps in dependencies.items():
        graph[key] = set(deps['attrDependencies'])

    # Helper function for DFS
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        order.append(node)

    # Perform DFS for each node
    for node in graph.keys():
        dfs(node)

    return order



class InterpreterGenerator:
    def __init__(self, semantics, attributes, symbols):
        self.attributes = attributes
        self.symbols = symbols
        self.functions=self.__generateFunctionsAll__(semantics)
        self.__checkUnusedAttributes__()
                

    def generateFunctionString(self, function, ident=4) -> str:
        funDef, code = function
        string = funDef.replace('\t', ' '*ident)
        for line in code:
            string += '\n'+line.replace('\t', ' '*ident)
        
        return string+'\n'

    # Generates the file that will be used to calculate the attributes, allowing the user to see the generated code
    def generateFile(self, ident=4, name="MyInterpreter") -> str:
        string = f"from lark import Lark, Token, Tree\nfrom lark.visitors import Interpreter\n\nclass {name}(Interpreter):"
        string += self.__helper_function_string__(ident)+'\n'
        string += '\n'.join([self.generateFunctionString(function, ident) for function in self.functions])
        return string

    # Generates the class that will be used to calculate the attributes, being able to be run at runtime
    def generateInterpreter(self, name='MyInterpreter') -> Interpreter:
        classString=self.generateFile(name=name)
        exec(classString, globals())
        instance = globals()[name]()
        return instance


    def __helper_function_string__(self, ident):
        return'''
\tdef __helper__(self, node):
\t\tpointers={}
\t\tpointers[node.data.split('_')[0]] = [node]
\t\tfor child in node.children:
\t\t\tname = ''
\t\t\tif type(child) == Tree:
\t\t\t\tname = child.data.split('_')[0]
\t\t\telif type(child) == Token:
\t\t\t\tname = child.type
\t\t\tif name not in pointers:
\t\t\t\tpointers[name] = []
\t\t\tpointers[name].append(child)
\t\treturn pointers
'''.replace('\t', ' '*ident)

    def __orderSemantics__(self, semantics, ruleName):
        #Dictionary with the dependencies of each semantic rule
        dependencies = {}

        #Auxiliary lists to help the ordering of the dependencies
        visit_aux = []
        full_visit_aux = []

        #Auxiliary list to store the inherited attributes
        inheritedAux = []

        for attributes, semantic in semantics:
            #If the semantic is an ER, the key is the first attribute
            if semantic['type'] == 'er':
                key=attributes[0]['value']
                start_idx=1
                #If the LHS is not an attribute of the node, the attribute is inherited
                if(attributes[0]['symbol'] != ruleName or attributes[0]['index'] > 0):
                    inheritedAux.append(attributes[0]['value'])
            
            #If the semantic is a TR or CC, the key is the whole line
            else:
                key=semantic['code']
                start_idx=0

            #If the key is not in the dependencies, add it
            if key not in dependencies:
                dependencies[key]={'expression':semantic['code'], 'attrDependencies':[], 'type':semantic['type'], 'attributes':attributes}
                if(semantic['type']=='cc'):
                    dependencies[key]['message']=semantic['message']

            for idx in range(0, len(attributes)):
                if(idx>=start_idx and attributes[idx]['value'] not in dependencies[key]['attrDependencies']):
                    dependencies[key]['attrDependencies'].append(attributes[idx]['value'])
                
                #This is an access to the entire list of nodes with the same symbol ($<symbol>), so all children with this symbol need to be visited
                if(attributes[idx]['index'] == -1 and (attributes[idx]['id'] not in full_visit_aux) and attributes[idx]['symbol'][0].islower()):
                    dependencies[attributes[idx]['value']]={'expression':f"[self.visit(x) for x in pointers['{attributes[idx]['symbol']}']]", 'attrDependencies':[], 'type':'visit', 'attributes':[]}
                    full_visit_aux.append(attributes[idx]['id'])

                #Add the visit to the child that holds the attribute, as it depends on it
                elif((attributes[idx]['symbol'] != ruleName or attributes[idx]['index'] > 0) and (attributes[idx]['id'] not in visit_aux and attributes[idx]['id'].split("[")[0] not in full_visit_aux) and attributes[idx]['symbol'][0].islower()):
                    dependencies[attributes[idx]['value']]={'expression':f"self.visit(pointers['{attributes[idx]['symbol']}'][{attributes[idx]['index']}])", 'attrDependencies':[], 'type':'visit', 'attributes':[]}
                    visit_aux.append(attributes[idx]['id'])


        
        for key, value in dependencies.items():

            for inherited in inheritedAux:
                if(value['type']=='visit' and key.split('.')[0]==inherited.split('.')[0] and not(inherited in value['attrDependencies'])):
                    value['attrDependencies'].append(inherited)



        order = topological_sort(dependencies)

        ordered_semantics = []

        for attribute in order:
            if(attribute in dependencies):
                ordered_semantics.append({'code':dependencies[attribute]['expression'], 'type':dependencies[attribute]['type'], 'attributes':dependencies[attribute]['attributes']})
                if(dependencies[attribute]['type']=='cc'):
                    ordered_semantics[-1]['message']=dependencies[attribute]['message']
                
        return ordered_semantics


    def __extractAttributes__(self, semantics, ruleName):
        #Create a regex to find all the attributes in the code, using the symbol table
        dynamic = '|'.join(self.symbols[ruleName])
        regex = fr'((?<!\w)({dynamic})(?!\w)(?:(?:\[(\d+)\])?\.([a-z][_a-zA-Z0-9]*))?)'
        pattern = re.compile(regex)
        attributes = pattern.findall(semantics['code'])

        res = []

        for match in attributes:
            # Index out of range verification
            if match[2]!= '':
                if int(match[2]) > semantics['code'].count(match[1]):
                    raise Exception("Index "+match[2]+" out of range for non-terminal "+match[1])            
            
            if match[3]!='' and match[3] not in self.attributes[match[1]]:
                raise Exception("Attribute "+match[3]+" not found in the attribute list of non-terminal "+match[1])
            
            elem = {'value':match[0], 'symbol':match[1], 'index':int(match[2])-1 if match[2]!='' else 0, 'attribute':match[3]}
            elem['id'] = elem['symbol'] + '[' + str(elem['index']) + ']'
            res.append(elem)

            if(elem['attribute'] != ''):
                self.attributes[elem['symbol']][elem['attribute']]['used'] += 1

        special_regex = fr'(@(?<!\w)({dynamic}))'
        special_pattern = re.compile(special_regex)
        special_attributes = special_pattern.findall(semantics['code'])

        for match in special_attributes:
            elem = {'value': match[0], 'symbol':match[1], 'index':-1, 'attribute':''}
            elem['id'] = elem['symbol']
            res.append(elem)

        return res
    
    def transformExpression(self, semanticDef, ruleName):
        aux_string=semanticDef['code']
        
        for attribute in semanticDef['attributes']:

            # Ensure that it matches with the entire value, without trailing or leading characters
            target = r'(?<!(@|\$|\w))'+ re.escape(attribute['value']) +r'\b'

            if(attribute['symbol'] == ruleName and attribute['index'] == 0):
                    if attribute['attribute'] == '':
                        aux_string = re.sub(target, 'node', aux_string)
                    else:
                        aux_string = re.sub(target, f"node.{attribute['attribute']}", aux_string)

            elif(attribute['index'] != -1):
                if attribute['attribute'] == '':
                    aux_string = re.sub(target, f"pointers['{attribute['symbol']}'][{attribute['index']}]", aux_string)
                else:
                    aux_string = re.sub(target, f"pointers['{attribute['symbol']}'][{attribute['index']}].{attribute['attribute']}", aux_string)

            else:
                aux_string = re.sub(target, f"pointers['{attribute['symbol']}']", aux_string)

        # Replace all $symbol occurrences with len(pointers['symbol'])
        dynamic = '|'.join(self.symbols[ruleName])
        regex = fr'(?<!\w)\$({dynamic})\b'
        pattern = re.compile(regex)
        aux_string = pattern.sub(lambda x: f"len(pointers['{x.group(1)}'])", aux_string)

        if semanticDef['type'] == 'cc':
            string = f"\t\tif(not({aux_string})):\n"
            string += f"\t\t\traise Exception(\"{semanticDef['message']}\")"
        else:
            string = f"\t\t{aux_string}"

        return string
    
    def __checkUnusedAttributes__(self):
        for symbol, attributes in self.attributes.items():
            for attribute, data in attributes.items():
                if data['used'] == 0:
                    warnings.warn(f"Attribute '{attribute}' of symbol '{symbol}' is defined but never used", Warning)


    def __generateFunctionsAll__(self, semantics):
        functions = []
        for ruleName, ruleSemantics in semantics.items():
            functions.extend(self.__generateFunctionsRule__(ruleSemantics, ruleName))
        return functions

    def __generateFunctionsRule__(self, ruleSemantics, ruleName):
        functions = []
        for expansionIndex, expansionSemantics in enumerate(ruleSemantics):
            functions.append(self.__generateFunctionExpansion__(expansionSemantics, expansionIndex, ruleName))
        return functions

    def __generateFunctionExpansion__(self, expansionSemantics, expansionIndex, ruleName):
        funDef = "\tdef "+ruleName+"_"+str(expansionIndex)+"(self, node):"

        code=[]
        code.append("\t\tpointers = self.__helper__(node)")

        aux=[]
        for semanticDef in expansionSemantics['semantics']:
            aux.append((self.__extractAttributes__(semanticDef, ruleName), semanticDef))

        
        ordered_semantics = self.__orderSemantics__(aux, ruleName)

        # Transform into code for ER, CC and TR
        for semanticDef in ordered_semantics:
            code.append(self.transformExpression(semanticDef, ruleName))


        return (funDef, code)