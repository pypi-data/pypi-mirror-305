
from lark import Lark
from .generator_layer import GeneratorLayer
from .processor_layer import ProcessorLayer

class Lark_AG:
    def __init__(self, grammar):
        self.generator = GeneratorLayer(grammar)
        self.processor = ProcessorLayer(self.generator.getCFG(), self.generator.getInterpreter())

    def process(self, input):
        return self.processor.process(input)
    
    def getCFG(self):
        return self.generator.getCFG()
    
    def getInterpreter(self):
        return self.generator.getInterpreter()
    
    def getInterpreterFile(self):
        return self.generator.getInterpreterFile()
    
    def getRootLevelAttributes(self):
        return self.generator.getRootLevelAttributes()