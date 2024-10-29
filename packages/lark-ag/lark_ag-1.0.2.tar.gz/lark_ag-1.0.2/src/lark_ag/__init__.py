''' LARK-AG: A Python library for providing Attribute Grammar support to Lark. '''

#Read version from pyproject.toml
from importlib.metadata import version
__version__ = "1.0.2"

from .generator_layer import GeneratorLayer
from .processor_layer import ProcessorLayer

from .lark_ag import Lark_AG

__all__ = ('GeneratorLayer', 'ProcessorLayer', 'Lark_AG')