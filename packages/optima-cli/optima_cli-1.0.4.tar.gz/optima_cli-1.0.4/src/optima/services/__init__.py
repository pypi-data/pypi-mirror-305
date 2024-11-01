# Import service modules
from . import api_client, db_services
from . import cli_handler, cli_messages, cli_prompts, cli_validation
from . import mf_upload, mf_utils

# Define what symbols should be exported when using "from frontend.src.services import *"
__all__ = [
    'api_client',
    'db_services',
    'cli_handler',
    'cli_messages',
    'cli_prompts',
    'cli_validation',
    'mf_upload',
    'mf_utils'
]

# Package metadata
__version__ = '0.1'
__package__ = 'frontend.src.services'
__author__ = 'OPTIMA'
__description__ = 'Service modules for OPTIMA Data Management CLI core functionality.'