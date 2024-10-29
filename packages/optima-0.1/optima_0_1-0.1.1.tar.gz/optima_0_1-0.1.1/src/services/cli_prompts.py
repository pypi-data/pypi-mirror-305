import sys

from services.cli_messages import show_options
from services.cli_validation import validate_selection


def request_user_input(
    prompt_msg: str,
    has_newline: bool = False,
    lower_case: bool = False,
    enter_enabled: bool = False,
    enter_action_desc: str = None,
) -> str:
    """Request user input with an optional newline before the prompt message."""
    if has_newline:
        user_input = input(f"\n{prompt_msg}").strip()
    else:
        user_input = input(f"{prompt_msg}").strip()
    return user_input.lower() if lower_case else user_input


def request_user_selection(
    options_desc: str, options: list, enter_enabled: bool = False, enter_action_desc: str = None
) -> int:
    """Request user selection from a list of options provided by the caller, with an optional Enter action."""

    # Ensure 'enter_action_desc' is provided if 'enter_enabled' is set to True
    if enter_enabled and not enter_action_desc:
        raise ValueError(
            "'enter_action_desc' must be a non-empty string when 'enter_enabled' is True."
        )

    show_options(options_desc, options)

    # Set selection prompt message based on options and 'enable_enter'
    if enter_enabled:
        if options:
            prompt_msg = f"Select an option by number (press Enter to {enter_action_desc}): "
        else:
            prompt_msg = f"Press Enter to {enter_action_desc}: "
    else:
        prompt_msg = "Select an option by number: "

    while True:
        selection = request_user_input(prompt_msg)
        if enter_enabled and selection == "":
            return -1  # Handle the special case when user pressed Enter
        if validate_selection(selection, len(options)):
            return int(selection) - 1  # Return the valid selection as an integer


def request_user_confirmation(prompt_msg: str) -> bool:
    """Request user for a yes/no confirmation based on the prompt message."""
    response = request_user_input(f"{prompt_msg} (y/n): ").lower()
    return response == "y"
