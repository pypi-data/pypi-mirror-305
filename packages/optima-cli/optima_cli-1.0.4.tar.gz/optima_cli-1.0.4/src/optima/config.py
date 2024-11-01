import logging
import os
from typing import Any
from dotenv import load_dotenv
import pkg_resources

# Load environment variables from .env file
# Try to load local .env first, then fall back to package .env
local_env = os.path.join(os.getcwd(), '.env')
if os.path.exists(local_env):
    load_dotenv(local_env)
else:
    # Fall back to package .env
    ENV_PATH = pkg_resources.resource_filename('optima', '.env')
    load_dotenv(ENV_PATH)

class Config:
    def __init__(self, env: str = os.getenv("CLI_ENV", "production")):
        self.api_prefix = os.getenv("API_PREFIX")
        
        # Set environment-specific configurations
        if env == "development":
            self.debug = True
            self.testing = False
            self.logging_level = logging.INFO
            self.api_base_url = os.getenv('LOCAL_API_BASE_URL')
            self.mf_dest_path = os.getenv("DEV_MF_DEST_PATH")
        elif env == "testing":
            self.debug = True
            self.testing = True
            self.logging_level = logging.DEBUG
            self.api_base_url = os.getenv('LOCAL_API_BASE_URL')
            self.mf_dest_path = os.getenv("TEST_MF_DEST_PATH")
        else:  # production
            self.debug = False
            self.testing = False
            self.logging_level = logging.CRITICAL
            self.api_base_url = os.getenv('AWS_API_BASE_URL')
            self.mf_dest_path = os.getenv("PROD_MF_DEST_PATH")

        self.full_api_url = f"{self.api_base_url}{self.api_prefix}"

# Global config instance
_config: Config | None = None

def get_config() -> Config:
    global _config
    if _config is None:
        _config = Config()
    return _config

def get_logger(name: str = __name__) -> logging.Logger:
    config = get_config()
    logging.basicConfig(
        level=config.logging_level,
        format="[%(levelname)s] %(filename)s: line %(lineno)d - %(message)s",
    )
    return logging.getLogger(name)

def get_api_base_url() -> str:
    return get_config().full_api_url

def get_api_prefix() -> str:
    return get_config().api_prefix

def get_mediaflux_dest_path() -> str:
    return get_config().mf_dest_path