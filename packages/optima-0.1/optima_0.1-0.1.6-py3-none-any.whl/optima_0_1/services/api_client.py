from typing import Dict, List, Tuple
from urllib.parse import quote

import requests

from ..constants import StatusAPI
from ..config import get_api_base_url, get_logger

logger = get_logger(__name__)
API_BASE_URL = get_api_base_url()


# ========================== API Resource Management ==========================
def create_resource(endpoint: str, data: dict) -> StatusAPI:
    """
    Create data to the database using the specified endpoint.

    Returns:
        - StatusAPI: StatusAPI.OK if successful, StatusAPI.ERROR otherwise.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    try:
        response = requests.request("POST", url, json=data)
        response.raise_for_status()
        return StatusAPI.OK
    except requests.exceptions.RequestException as e:
        if response:
            logger.error(f"{e}")
            logger.error(response.json().get("message"))
        else:
            logger.error(f"{e}")
        return StatusAPI.ERROR


def update_resource(endpoint: str, data: dict) -> StatusAPI:
    """
    Upload data to the database using the specified endpoint.

    Returns:
        - StatusAPI: StatusAPI.OK if successful, StatusAPI.ERROR otherwise.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    try:
        response = requests.request("PUT", url, json=data)
        response.raise_for_status()
        return StatusAPI.OK
    except requests.exceptions.RequestException as e:
        if response:
            logger.error(f"{e}")
            logger.error(response.json().get("message"))
        else:
            logger.error(f"{e}")
        return StatusAPI.ERROR


def get_resource(endpoint: str) -> Tuple[StatusAPI, requests.Response]:
    """
    Returns:
        - requests.Response: The response object if the status is 200, 201 or 404.
        - StatusAPI.ERROR: If the status is none of above.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    try:
        response = requests.request("GET", url)
        response.raise_for_status()
        return (StatusAPI.OK, response)
    except requests.exceptions.RequestException as e:
        if e.response.status_code == 404:
            logger.warning(f"Ignoring: {e}.")
            return (StatusAPI.NOT_FOUND, None)
        else:
            logger.error(f"{e}")
            if response:
                logger.error(response.json().get("message"))
            return (StatusAPI.ERROR, None)


# ========================== User-related Functions ==========================
def fetch_user_id_by_username(username) -> int | StatusAPI:
    """
    Retrieve user ID by username from the API.

    Returns:
        - int: The user ID if found.
        - StatusAPI.NOT_FOUND: If the user doesn't exist.
    """
    status, response = get_resource(endpoint=f"users/id_by_username?username={quote(username)}")
    if status == StatusAPI.OK:
        return response.json().get("data").get("id")
    return status


def fetch_user_id_and_domain_by_username(username) -> Tuple[int, str] | StatusAPI:
    """
    Retrieve user ID and domain by username from the API.

    Returns:
        - Tuple[int, str]: A tuple containing (user_id, domain) if found.
        - StatusAPI.NOT_FOUND: If the user doesn't exist.
    """
    status, response = get_resource(
        endpoint=f"users/id_domain_by_username?username={quote(username)}"
    )
    if status == StatusAPI.OK:
        user_data = response.json().get("data")
        return (user_data.get("id"), user_data.get("domain"))
    return status


# ========================== Problem-related Functions ==========================
def fetch_all_problems() -> Dict[int, str] | StatusAPI:
    """
    Retrieve all problems from the API.

    Returns:
        - Dict[int, str]: A dictionary mapping problem IDs to their full names.
        - StatusAPI.ERROR: If an error occurred during the API request.
    """
    status, response = get_resource(endpoint="problems")
    if status == StatusAPI.OK:
        all_problems = response.json().get("data")
        return all_problems
    return status


def fetch_problem_info(full_name) -> Tuple[int, str, str, str, str] | StatusAPI:
    """
    Retrieve detailed problem information by its full name from the API.

    Returns:
        - Tuple[int, str, str, str, str]: A tuple containing (id, abbr_name, instance_suffix, metadata_csv, readme).
        - StatusAPI.NOT_FOUND: If the problem doesn't exist.
    """
    status, response = get_resource(endpoint=f"problems/by_name/{quote(full_name)}")
    if status == StatusAPI.OK:
        prob_data = response.json().get("data")
        return (
            prob_data.get("id"),
            prob_data.get("problem_abbr_name"),
            prob_data.get("instance_suffix"),
            prob_data.get("metadata_csv"),
            prob_data.get("readme"),
        )
    return status


def fetch_problem_by_id(problem_id) -> dict | StatusAPI:
    """
    Retrieve problem details by its ID from the API.

    Returns:
        - dict: A dictionary containing problem details.
        - StatusAPI.ERROR: If an error occurred during the API request.
    """
    status, response = get_resource(endpoint=f"problems/{problem_id}")
    if status == StatusAPI.OK:
        return response.json().get("data")
    return status


def query_instance_category_from_db(problem_id) -> List[str] | StatusAPI:
    """
    Retrieve instance category for a given problem by ID from the API.

    Returns:
        - List[str]: A list of instance categories if successful,
        - StatusAPI.ERROR: If an error occurred during the API request.
    """
    status, response = get_resource(endpoint=f"instances/category/{problem_id}")
    if status == StatusAPI.OK:
        return response.json().get("data").get("categories")
    return status


def fetch_all_problem_types() -> Dict[int, str] | StatusAPI:
    """
    Retrieve all problem types from the API.

    Returns:
        - Dict[int, str]: A dictionary mapping problem type IDs to their names.
        - StatusAPI.ERROR: If an error occurred during the API request.
    """
    status, response = get_resource(endpoint="problem_types")
    if status == StatusAPI.OK:
        prob_types = {int(type["id"]): type["type_name"] for type in response.json().get("data")}
        return prob_types
    return status


def fetch_problem_by_abbr(abbr: str):
    status, response = get_resource(endpoint=f"problems/by_abbr?problem_abbr_name={quote(abbr)}")
    if status == StatusAPI.OK:
        return response.json().get("data")
    return status


