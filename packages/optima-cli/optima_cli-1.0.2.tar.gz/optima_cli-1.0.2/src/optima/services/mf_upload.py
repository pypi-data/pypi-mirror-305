import os
import re
import shutil
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

from ..config import get_logger

logger = get_logger()

from ..constants import MF_UPLOAD_EXECUTABLE, FileType, StatusMF
from .mf_utils import MF_CONFIG_FILE_PATH, MF_DEST_PARENT_PATH
from .mf_utils import LOG_DIR, TMP_DIR, create_dir
from .api_client import query_instance_category_from_db


# ========================= Before MediaFlux Upload =========================
def classify_instance_category(
    file_path: str, problem_id: int
) -> Tuple[Dict[str, List[str]], Set[str]]:
    """
    Categorize uploaded files and handle mismatched categories.

    - param file_path: Path to the file or directory to categorize
    - param problem_id: ID of the problem

    - return: Dictionary of categories and their file paths
    """

    def _categorize_single_instance_file(file_path: str) -> Dict[str, List[str]]:
        """Categorize a single instance file."""
        category = os.path.basename(os.path.dirname(file_path))
        return {category: [file_path]}

    def _categorize_instance_directory(directory_path: str) -> Dict[str, List[str]]:
        """Categorize all instance files within a directory."""
        categorized_files = {}
        for root, _, files in os.walk(directory_path):
            category = os.path.basename(root)
            categorized_files[category] = [
                os.path.join(root, file)
                for file in files
                if not file.startswith(".")  # Ignore all hidden files
            ]
        return categorized_files

    # Categorize instance based on file/directory
    categorized_instances: Dict[Optional[str], List[str]] = {}
    if os.path.isdir(file_path):
        categorized_instances = _categorize_instance_directory(file_path)
    elif os.path.isfile(file_path):
        categorized_instances = _categorize_single_instance_file(file_path)

    # Get existing categories from the database for the given problem ID
    existing_categories = set(query_instance_category_from_db(problem_id))
    new_categories = set(categorized_instances.keys()) - existing_categories
    return (categorized_instances, new_categories)


def copy_instances_to_tmp(instances_by_category: Dict[str, List[str]]) -> str:
    """
    Copy instance files to a temporary folder, organizing them by category.
    """
    tmp_instances_folder = os.path.join(TMP_DIR, FileType.INSTANCE.value)
    create_dir(folder_path=tmp_instances_folder, folder_desc="temporary instances folder")

    success_count, fail_count = 0, 0
    for category, instances in instances_by_category.items():
        # If no category and only a single/single set of instances
        if category is None and len(instances_by_category) == 1:
            category_folder = tmp_instances_folder
        else:
            category_folder = os.path.join(tmp_instances_folder, category)
        create_dir(folder_path=category_folder, folder_desc="temporary category folder")

        # Copy all instances with resoloved categories to temporary instances folder
        for instance in instances:
            file_name = os.path.basename(instance)
            destination_path = os.path.join(category_folder, file_name)
            try:
                shutil.copy2(instance, destination_path)
                success_count += 1
            except OSError as e:
                logger.warning(f"Failed to copy '{file_name}' to '{destination_path}': {e}")
                fail_count += 1

    logger.info(f"Copy operation completed: {success_count} files copied, {fail_count} failures.")
    return category_folder


def create_tmp_problem_dir(prob_abbr: str) -> str:
    """
    Create a temporary folder for a problem with designed structures.
    """
    tmp_problem_folder = os.path.join(TMP_DIR, prob_abbr)
    instances_folder = os.path.join(tmp_problem_folder, FileType.INSTANCE.value)
    create_dir(folder_path=instances_folder, folder_desc="temporary problem folder")
    return tmp_problem_folder


# ========================= Upload to MediaFlux =========================
def build_mf_upload_command(mf_dest_path: str, src_path: str, nb_workers: Optional[int] = 4) -> str:
    """
    Build and execute MediaFlux upload command for problem instances.
    """
    # Create log directory if it doesn't exist
    create_dir(LOG_DIR, "log folder")

    # Build the upload command
    mf_destination_path = os.path.join(MF_DEST_PARENT_PATH, mf_dest_path)
    command = f"{MF_UPLOAD_EXECUTABLE} --mf.config {MF_CONFIG_FILE_PATH} --csum-check --nb-workers {nb_workers} --dest {mf_destination_path} {src_path} --log-dir {LOG_DIR}"
    return command


# ========================= After MediaFlux Upload: Parse/Filter Results =========================
def parse_mf_upload_counts(log_content: str) -> Dict[StatusMF, int]:
    """
    Parse MediaFlux upload results to extract counts of uploaded, skipped, and failed files.
    """
    mf_status_count_pattern = {
        StatusMF.UPLOAD: r"Uploaded files:\s+([\d,]+)\s*files",
        StatusMF.SKIP: r"Skipped files:\s+([\d,]+)\s*files",
        StatusMF.FAIL: r"Failed files:\s+([\d,]+)\s*files",
    }

    counts = {status: 0 for status in StatusMF.list()}
    for mf_status, count in mf_status_count_pattern.items():
        match = re.search(count, log_content)
        counts[mf_status] = int(match.group(1).replace(",", ""))

    logger.info(f"MF Status: {counts}")
    return counts


def parse_mf_uploaded_files(log_content: str) -> List[Dict[str, str]]:
    """
    Parse MediaFlux upload results to extract local and MediaFlux paths of uploaded files.

    - return: List of dictionaries containing local and MediaFlux paths
    """
    # RegEx to match uploaded file paths and their MediaFlux paths
    uploaded_file_path_pattern = re.compile(r"Uploaded file: '(.+?)' to asset\(id=\d+\): '(.+?)'")

    # Build a list of dictionaries for local and Mediaflux paths
    uploaded_files = uploaded_file_path_pattern.findall(log_content)
    uploaded_files_details = [
        {"local_path": local_path, "mediaflux_path": mediaflux_path}
        for local_path, mediaflux_path in uploaded_files
    ]
    return uploaded_files_details


def filter_mf_uploaded_files(
    instances_by_category: Dict[str, List[str]], uploaded_file_details: List[Dict[str, str]]
) -> Dict[str, List[str]]:
    """
    Filter uploaded files based on instance categories and extracted information.

    - return: Filtered dictionary of categories and their file paths
    """
    # Extract file paths and names from uploaded file details from MediaFlux
    uploaded_file_paths, uploaded_file_names = set(), set()
    for uploaded_file in uploaded_file_details:
        local_path = uploaded_file["local_path"]
        file_name = os.path.basename(local_path)
        dir_name = os.path.basename(os.path.dirname(local_path))

        # Store combined directory and file names for path matching
        uploaded_file_paths.add(os.path.join(dir_name, file_name))
        uploaded_file_names.add(file_name)

    # Iterate through each category and its instances
    filtered_dict = {}
    for category, instances in instances_by_category.items():
        filtered_instances = []

        # Check each instance to see if it matches an uploaded file
        for instance in instances:
            file_name = os.path.basename(instance)
            if category is not None:
                # Check if the instance file path matches any uploaded file paths
                if os.path.join(category, file_name) in uploaded_file_paths:
                    filtered_instances.append(instance)
            else:
                # For uncategorized files, check if the instance file name matches any uploaded file names
                if file_name in uploaded_file_names:
                    filtered_instances.append(instance)

        # Only add categories with matching instances to the filtered dictionary
        if filtered_instances:
            filtered_dict[category] = filtered_instances

    # Return the filtered dictionary or None if it contains no matches
    return filtered_dict if filtered_dict else None
