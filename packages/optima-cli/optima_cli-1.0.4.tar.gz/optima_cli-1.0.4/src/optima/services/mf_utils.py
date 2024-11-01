import glob
import os
import shutil

from ..config import get_logger, get_mediaflux_dest_path

logger = get_logger(__name__)

# Path in Mediaflux where files will be uploaded
MF_DEST_PARENT_PATH = get_mediaflux_dest_path()

# MediaFlux configuration file settings (mflux.cfg)
MF_CONFIG_FILE_PATH = os.path.join(os.getcwd(), "mflux.cfg")
MF_CONFIG_FILE = {
    "host": "mediaflux.researchsoftware.unimelb.edu.au",
    "port": 443,
    "transport": "https",
}

# Directories for logging and temporary files
LOG_DIR = "./log"
TMP_DIR = "./tmp"


# ========================= MediaFlux Configuration File =========================
def update_mf_config_file(
    domain: str,
    username: str,
) -> None:
    """
    Update the Mediaflux configuration file with domain and username.
    """
    # Open the config file for writing (creates it if it doesn't exist)
    with open(MF_CONFIG_FILE_PATH, "w") as config_file:
        for key, value in MF_CONFIG_FILE.items():
            config_file.write(f"{key.lower()}={value}\n")
        config_file.write(f"domain={domain}\n")
        config_file.write(f"user={username}\n")


def reset_mf_config_file() -> None:
    """
    Reset the Mediaflux configuration file by clearing domain and username.
    """
    update_mf_config_file("", "")


# ========================= MediaFlux Log, Temporary Directory =========================
def mf_read_operation_log() -> str:
    """
    Read the latest log file.

    Returns:
        - str: The content of the latest log file if successful.
        - None: If no log files exist or an error occurs.
    """
    try:
        log_files = glob.glob(os.path.join(LOG_DIR, "*.log"))
        latest_log_file = max(log_files, key=os.path.getmtime)
        with open(latest_log_file, "r") as file:
            log_content = file.read()
        logger.info(f"Read MF execution log file '{latest_log_file}'.")
        return log_content
    except Exception as e:
        logger.error(f"Failed to read MediaFlux execution log file '{latest_log_file}': {e}.")
        raise


def mf_clean_up(tmp_dir: bool = False, log_dir: bool = False):
    reset_mf_config_file()
    if tmp_dir:
        delete_dir(folder_path=TMP_DIR, folder_desc="MediaFlux temporary folder")
    if log_dir:
        delete_dir(folder_path=LOG_DIR, folder_desc="MeidaFlux log folder")


# ========================= Directory/File Management =========================
def create_dir(folder_path: str, folder_desc: str) -> None:
    """Create a directory if it doesn't exist."""
    try:
        os.makedirs(folder_path, exist_ok=True)
        logger.info(f"Created {folder_desc} '{folder_path}'.")
    except OSError as e:
        logger.error(f"Failed to create {folder_desc} '{folder_path}': {e}.")


def delete_dir(folder_path: str, folder_desc: str) -> None:
    """Delete a directory and its contents."""
    try:
        shutil.rmtree(folder_path)
        logger.info(f"Deleted {folder_desc} '{folder_path}'.")
    except OSError as e:
        logger.error(f"Failed to delete {folder_desc} '{folder_path}': {e}.")
