class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


def show_message(message: str) -> None:
    """Print a generic message without additional formatting to the user."""
    print(f"{message}")


def show_success(message: str) -> None:
    """Print a success prefix in green to inform the user of positive outcomes."""
    print(f"{Colors.GREEN}SUCCESS: {Colors.RESET} {message}")


def show_error(message: str) -> None:
    """Print an error prefix in red to alert the user about an issue."""
    print(f"{Colors.RED}ERROR: {Colors.RESET} {message}")


def show_info(message: str) -> None:
    """Print an info prefix in blue to provide context to the user."""
    print(f"{Colors.BLUE}INFO: {Colors.RESET} {message}")


def show_warning(message: str) -> None:
    """Print a warning prefix in yellow to notify the user of potential issues."""
    print(f"\n{Colors.YELLOW}WARNING: {Colors.RESET} {message}")


def show_options(options_description: str, options: list) -> None:
    """Print the options description and option index in cyan color."""
    print(f"\nAvailable {Colors.CYAN}{options_description} {Colors.RESET}")

    if not options:
        show_info("Nothing available now.")

    for idx, option in enumerate(options, 1):
        print(f"{Colors.CYAN}{idx}.{Colors.RESET} {option}")


def show_items(items: list) -> None:
    """Print the item index with item in red color."""
    for idx, item in enumerate(items, 1):
        print(f"{Colors.RED}{idx}.{Colors.RESET} {item}")

def show_splitter() -> None:
    """Print a separator line in a distinct style."""
    print(f"\n{Colors.BLUE}{'=' * 50}{Colors.RESET}\n")


def show_exit():
    """Print an exit message indicating the operation was terminated by user in yellow."""
    print(f"\n\n{Colors.YELLOW}Oops! It looks like you terminated the operation. Exiting now... {Colors.RESET}")
