import os
from typing import Dict, List, Optional

from ..constants import StatusAPI
from .api_client import create_resource, update_resource
from ..config import get_logger

logger = get_logger(__name__)


# ========================== User Creation ==========================
def db_create_user(username, domain, email=None) -> bool:
    """
    Create a new user with the given username, domain, and optional email.

    Returns:
        - StatusAPI.OK: If the user was created successfully.
    """
    user_data = {"username": username, "domain": domain, "email": email or None}
    db_result = create_resource(endpoint="users", data=user_data)
    return db_result == StatusAPI.OK

# ========================== Problem Creation Operation ==========================
def db_create_problem(
    user_id: int,
    prob_full_name: str,
    prob_abbr_name: str,
    prob_type_id: int,
    instance_suffix: str,
    metadata_file: Optional[str] = None,
    readme_file: Optional[str] = None,
) -> bool:
    """
    Create a new problem in the database.
    """
    problem_data = {
        "problem_full_name": prob_full_name,
        "problem_abbr_name": prob_abbr_name,
        "creator_id": user_id,
        "problem_type_id": prob_type_id,
        "instance_suffix": instance_suffix,
        "metadata_csv": metadata_file,
        "readme": readme_file
    }
    db_result = create_resource(endpoint="problems", data=problem_data)
    logger.info(f"DB Status - Problem Creation: {db_result}. ")
    return db_result == StatusAPI.OK


# ========================== Upload Operation ==========================
def db_create_or_update_instances(
    user_id: int, problem_id: int, instances_grouped_by_category: Dict[str, List[str]]
) -> int:
    """
    Upload instance files to the database and track results.
    """
    db_counts = {StatusAPI.OK: 0, StatusAPI.ERROR: 0}
    for category, instances in instances_grouped_by_category.items():
        db_counts[category] = []
        for instance in instances:
            instance_data = {
                "instance_name": os.path.basename(instance),
                "creator_id": user_id,
                "problem_id": problem_id,
                "shared_link": None,
                "instance_category": category or None,
            }
            db_result = create_resource(endpoint="instances", data=instance_data)
            db_counts[db_result] += 1
    logger.info(f"DB Status - Instances: {db_counts}")
    return db_counts[StatusAPI.OK]


def db_update_readme(problem_id: int, src_path: str) -> bool:
    """
    Handle the upload of readme file to the database.
    """
    file_name = os.path.basename(src_path)
    problem_data = {"readme": file_name}
    db_result = update_resource(endpoint=f"problems/{problem_id}", data=problem_data)
    logger.info(f"DB Status - README: {db_result}. ")
    return db_result == StatusAPI.OK


def db_update_metadata(problem_id: int, src_path: str) -> bool:
    """
    Handle the upload of metadata_csv file to the database.
    """
    file_name = os.path.basename(src_path)
    problem_data = {"metadata_csv": file_name}
    db_result = update_resource(endpoint=f"problems/{problem_id}", data=problem_data)
    logger.info(f"DB Status - METADATA: {db_result}. ")
    return db_result == StatusAPI.OK
