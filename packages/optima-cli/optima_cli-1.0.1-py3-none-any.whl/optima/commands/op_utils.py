from typing import Optional, Tuple

from ..constants import StatusAPI
from ..services.cli_handler import prompt_for_username, prompt_for_domain
from ..services.api_client import fetch_user_id_and_domain_by_username, fetch_user_id_by_username
from ..services.db_services import db_create_user
from ..config import get_logger

logger = get_logger(__name__)


def get_or_prompt_user_info(
    username: Optional[str], domain: Optional[str] = None
) -> Tuple[Optional[int], str, str]:
    """Retrieve user information based on the provided username and domain."""
    # If both username and domain are provided, return user_id as None
    if username and domain:
        user_id = None
        return (user_id, username, domain)

    # Prompt for username if not provided, and attemp to fetch user ID and domain from API
    username = prompt_for_username(username)
    requested_user_data = fetch_user_id_and_domain_by_username(username)

    if requested_user_data == StatusAPI.NOT_FOUND:
        user_id, domain = (None, prompt_for_domain())
    else:
        user_id, domain = requested_user_data

    return (user_id, username, domain)


def create_new_user(username: str, domain: str, user_id: Optional[int]) -> int:
    """Ensure the user exists in the system, creating if necessary."""
    if user_id is None:
        db_create_user(username=username, domain=domain)
        user_id = fetch_user_id_by_username(username)
        return user_id
    else:
        return user_id
