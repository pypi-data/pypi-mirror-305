from typing import Dict, List, Optional

from ..constants import FileType, StatusAPI
from .api_client import fetch_problem_info, fetch_all_problems, fetch_all_problem_types, fetch_problem_by_abbr
from .cli_messages import show_error, show_info, show_warning
from .cli_prompts import request_user_input, request_user_selection
from .cli_validation import *


# ========================== User Information ==========================
def prompt_for_username(username: Optional[str]) -> str:
    """Return the given MediaFlux username if valid; otherwise, prompt for a valid one."""
    if username and validate_username(username):
        return username.lower()
    while True:
        username = request_user_input(
            "Enter your MediaFlux username: ", lower_case=True, has_newline=True
        )
        if validate_username(username):
            return username


def prompt_for_domain() -> str:
    """Prompt for a valid MediaFlux domain."""
    while True:
        domain = request_user_input(
            "Enter your MediaFlux domain (student/staff): ", lower_case=True
        )
        if validate_domain(domain):
            return domain


def prompt_for_email() -> str:
    """Prompt for a valid email address."""
    while True:
        email = request_user_input(
            "Enter your email (optional; press Enter to skip): ", lower_case=True
        )
        if email == "":
            return None
        if validate_email(email):
            return email


# ========================== Upload Instance ==========================
def select_upload_file_type() -> FileType:
    """Present and handle user selection for upload file type."""
    options = FileType.list()
    selection = request_user_selection("Upload Types", options)
    return options[selection]


def select_problem(prob_abbr: Optional[str]) -> str:
    """Present a list of problems by name and handle user selection or new problem creation."""
    if prob_abbr and fetch_problem_by_abbr(prob_abbr) != StatusAPI.NOT_FOUND:
        return prob_abbr
    problems = fetch_all_problems()
    problems_dict = {f"{problem['problem_full_name']}: {problem['problem_abbr_name']}": problem['problem_abbr_name'] for problem in problems}
    options = list(problems_dict.keys())
    selection = request_user_selection(
        "Problems", options, enter_enabled=True, enter_action_desc="create a problem"
    )
    if selection == -1:
        return "Create New Problem"
    else:
        selected_problem_name = options[selection]  # Get the name of the selected problem
        return problems_dict[selected_problem_name] 


def prompt_for_instances_path(file_path: Optional[str], instance_suffix: str) -> str:
    """Prompt and validate user input for file/folder path to upload."""
    if file_path and validate_upload_instance_files(file_path, instance_suffix):
        return file_path
    while True:
        show_warning("Folders will be treated as instance categories.")
        file_path = request_user_input("Enter the path to the file/folder to upload: ")
        if validate_upload_instance_files(file_path, instance_suffix):
            return file_path


def select_mismatched_category_action(
    detected_category: str, instances_grouped_by_category: Dict[str, List[str]]
) -> Dict[Optional[str], List[str]]:
    """Present options and handle user input for mismatched categories."""
    options = {
        "keep": f"Keep '{detected_category}'",
        "rename": "Rename Category",
        "remove": "No Category",
    }
    option_actions = list(options.keys())
    selection = request_user_selection("Actions", list(options.values()))

    if option_actions[selection] == "keep":
        show_info(f"Category '{detected_category}' has been kept.")
        return instances_grouped_by_category
    elif option_actions[selection] == "rename":
        new_category = request_user_input("Enter the new category name: ")
        if new_category and new_category != detected_category:
            show_info(f"Category '{detected_category}' has been renamed to '{new_category}'.")
            instances_grouped_by_category[new_category] = instances_grouped_by_category.pop(detected_category)
        else:
            show_info(f"Category name unchanged. Keeping '{detected_category}'.")
    elif option_actions[selection] == "remove":
        show_info(f"Category '{detected_category}' has been removed.")
        instances_grouped_by_category[None] = instances_grouped_by_category.pop(detected_category)

    return instances_grouped_by_category


# ========================== Upload Metada/README ==========================


def prompt_for_single_upload_path(file_path: Optional[str], required_suffix: str) -> str:
    """Prompt and validate user input for file path to upload."""
    if (
        file_path
        and validate_path_exists(file_path)
        and validate_file_suffix(file_path, required_suffix)
    ):
        return file_path
    while True:
        file_path = request_user_input("Enter the path to the file to upload: ")
        if validate_path_exists(file_path) and validate_file_suffix(file_path, required_suffix):
            return file_path


# ========================== Problem Creation ==========================
def prompt_for_prob_full_name() -> str:
    """Prompt, validate, and format user input for a new problem name."""

    def _format_problem_name(entered_problem_name: str) -> str:
        """Format problem name by capitalizing words and removing delimiters."""
        words = re.split(r"[-_\s]+", entered_problem_name)  # Split by space, hyphen, or underscore
        return "".join(word.capitalize() for word in words)

    while True:
        problem_name = request_user_input("Enter a problem name: ", has_newline=True)
        problem_name = _format_problem_name(problem_name)
        if validate_prob_full_name(problem_name):
            response = fetch_problem_info(problem_name)
            if response == StatusAPI.NOT_FOUND:
                return problem_name
            else:
                show_error("This problem name already exists. Please enter a different one.")


def prompt_for_prob_abbr_name(full_name: str) -> str:
    """Prompt for problem abbreviation, suggesting one based on full name."""

    def _create_problem_abbr(formatted_name: str) -> str:
        """Create a problem abbreviation from a formatted problem name."""
        words = re.findall(r"[A-Z][a-z]", formatted_name)
        if len(words) > 1:
            return "".join(word[0].lower() for word in words)
        else:
            return formatted_name[:4].lower()

    while True:
        suggested_abbr = _create_problem_abbr(full_name)
        
        # If problem abbr not exist
        prob_data = fetch_problem_by_abbr(suggested_abbr)
        if prob_data == StatusAPI.NOT_FOUND:
            show_info(f"Suggested abbreviation: '{suggested_abbr}'")
            new_abbr = request_user_input("Enter a problem abbreviation (press Enter to accept): ")
            if new_abbr == "" or new_abbr == suggested_abbr:
                return suggested_abbr
            else:
                if validate_prob_abbr_name(new_abbr):
                    return new_abbr
        
        # Otherwise, problem abbr exist
        else:
            new_abbr = request_user_input("Enter a problem abbreviation: ")
            if validate_prob_abbr_name(new_abbr):
                prob_data = fetch_problem_by_abbr(new_abbr)
                if prob_data == StatusAPI.NOT_FOUND:
                    return new_abbr
                else:
                    prob_full_name = prob_data.get("problem_full_name")
                    show_error(f"Abbreviation '{new_abbr}' exists for problem '{prob_full_name}'.")

def prompt_for_prob_instance_suffix() -> str:
    """Prompt and validate user input for problem instance file format."""
    while True:
        suffix = request_user_input(
            "Enter the instance file format: ",
            has_newline=True,
        )
        if suffix.startswith("."):
            suffix = suffix[1:]  # Remove leading dot
        if validate_prob_instance_suffix(suffix):
            return suffix


def select_prob_type() -> str:
    """Present problem type options and handle user selection."""
    all_prob_types = fetch_all_problem_types()
    options = list(all_prob_types.values())
    selection = request_user_selection("Problem Types", options)
    return list(all_prob_types.keys())[selection]
