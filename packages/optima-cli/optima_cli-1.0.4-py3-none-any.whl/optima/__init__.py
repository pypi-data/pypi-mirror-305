# Import commands and CLI modules
from .cli import cli

# Define what symbols should be exported when using "from frontend.src import *"
__all__ = [
    'cli',
]

# Package metadata
__version__ = '0.1'
__package__ = 'frontend.src'
__author__ = 'OPTIMA'
__description__ = 'OPTIMA Data Management CLI: Easily manage your optimization research data.'