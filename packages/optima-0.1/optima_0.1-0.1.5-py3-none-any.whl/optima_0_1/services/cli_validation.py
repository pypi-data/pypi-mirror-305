import os
import re

from .cli_messages import show_error, show_items, show_message

MAX_DISPLAY_COUNT = 5


# ========================== User-related ==========================
def validate_username(username) -> bool:
    """Checks if username starts with a letter and contains only alphanumeric characters."""
    if not re.match("^[a-zA-Z][a-zA-Z0-9]*$", username):
        show_error("Username contains only letters and numbers.")
        return False
    return True


def validate_domain(domain) -> bool:
    """Checks if the domain is either 'student' or 'staff' (case-insensitive)."""
    if domain not in ["student", "staff"]:
        show_error("Domain must be 'student' or 'staff'.")
        return False
    return True


def validate_email(email) -> bool:
    """Checks if the email matches a standard email format using regex."""
    if not re.match(r"^[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$", email):
        show_error("Invalid email format.")
        return False
    return True


# ========================== Problem-related ==========================
def validate_prob_full_name(full_name) -> bool:
    """Checks if problem full name contains only letters, numbers, spaces, and hyphens."""
    if not re.match("^[a-zA-Z0-9\s\-]+$", full_name):
        show_error("Problem name must only contain letters and numbers.")
        return False
    return True


def validate_prob_abbr_name(abbr_name) -> bool:
    """Checks if problem abbreviation is >1 char long and contains only lowercase letters and numbers."""
    if len(abbr_name) <= 1:
        show_error("Problem abbreviation must be longer than 1 character.")
        return False
    if not re.match("^[a-z0-9]+$", abbr_name):
        show_error("Problem abbreviation must only contain letters and numbers.")
        return False
    return True


def validate_prob_instance_suffix(suffix) -> bool:
    """Checks if the problem instance suffix is longer than 1 character."""
    if len(suffix) <= 1:
        show_error("Problem instance file format must be longer than 1 character.")
        return False
    return True


# ========================== Instance-related ==========================
def validate_file_suffix(file_path: str, required_suffix: str) -> bool:
    """Checks if the file path ends with the required suffix"""
    if not file_path.endswith(required_suffix):
        show_error(f"File DOES NOT have the required suffix '{required_suffix}'.")
        return False
    return True


def validate_dir_suffix(dir_path: str, required_suffix: str) -> bool:
    """Checks if all files in directory path ends with the required suffix"""
    invalid_files = [
        f for f in os.listdir(dir_path) if not f.endswith(required_suffix) and not f.startswith(".")
    ]
    if invalid_files:
        show_error(f"The following files DO NOT have the required suffix '{required_suffix}': ")
        if len(invalid_files) > MAX_DISPLAY_COUNT:
            show_items(invalid_files[:MAX_DISPLAY_COUNT])
            show_message(f"...and {len(invalid_files) - MAX_DISPLAY_COUNT} more files not listed.")
        else:
            show_items(invalid_files)
        return False
    return True


# ========================== Instances-related ==========================
def validate_upload_instance_files(local_path: str, required_suffix: str) -> bool:
    """Checks if the given path exists and has the required file suffix."""
    if not validate_path_exists(local_path):
        return False
    if os.path.isfile(local_path):
        return validate_file_suffix(local_path, required_suffix)
    else:
        return validate_dir_suffix(local_path, required_suffix)


# ========================== General Usage ==========================
def validate_selection(selection: str, options_length: int) -> bool:
    """Checks if the selection is a valid integer within the range of available options."""
    try:
        selection_number = int(selection)
        if 1 <= selection_number <= options_length:
            return True
        else:
            show_error(f"Number must be between 1 and {options_length}.")
            return False
    except ValueError:
        show_error("A valid number is required.")
        return False


def validate_path_exists(local_path) -> bool:
    """Checks if the specified local file or directory path exists."""
    if not os.path.exists(local_path):
        show_error(f"Local path '{local_path}' does not exist.")
        return False
    return True
