import sys

from ..services.api_client import fetch_all_problems, fetch_all_problem_types
from ..services.cli_messages import show_options, show_exit, show_error
from ..config import get_logger

logger = get_logger()

def view_problems() -> None:
    try:
        problems = fetch_all_problems()
        problems_names = [f"{problem['problem_full_name']}: {problem['problem_abbr_name']}" for problem in problems]
        show_options("Problems", list(problems_names))
    except KeyboardInterrupt:
        show_exit()
        sys.exit(1)
    except Exception as e:
        logger.error(e)
        show_error("An unexpected error has occurred. Please try again.")
        sys.exit(1)

def view_problem_types() -> None:
    try:
        problem_types = fetch_all_problem_types()
        show_options("Problems", list(problem_types.values()))
    except KeyboardInterrupt:
        show_exit()
        sys.exit(1)
    except Exception as e:
        logger.error(e)
        show_error("An unexpected error has occurred. Please try again.")
        sys.exit(1)
    