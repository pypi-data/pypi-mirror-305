import sys
from typing import Optional, Tuple

from commands.op_utils import create_new_user, get_or_prompt_user_info
from services.cli_handler import *
from services.cli_messages import show_success, show_exit, show_splitter
from services.db_services import db_create_problem
from services.mf_upload import *
from services.mf_utils import mf_clean_up, update_mf_config_file
from config import get_logger

logger = get_logger(__name__)


def create_problem(
    username: Optional[str] = None,
    domain: Optional[str] = None,
    prob_full_name: Optional[str] = None,
) -> Tuple[int, str, str, str, Optional[int]]:
    """Main function to handle problem creation process."""
    try:
        # Step 1: User Inoformation
        user_id, username, domain = get_or_prompt_user_info(username, domain)

        # Step 2: Problem Information: full name, abbr name, instance suffix, problem type
        prob_full_name = prob_full_name or prompt_for_prob_full_name()
        prob_abbr = prompt_for_prob_abbr_name(prob_full_name)
        prob_instance_suffix = prompt_for_prob_instance_suffix()
        prob_type_id = select_prob_type()

        update_mf_config_file(username=username, domain=domain)
        # Step 4: Build MF execution command
        src_path = create_tmp_problem_dir(prob_abbr)
        mf_command = build_mf_upload_command(mf_dest_path="", src_path=src_path)

        # Step 5: Execute MF command
        show_splitter()
        mf_command_result = os.system(mf_command)
        show_splitter()
        
        # MediaFlux Command Executed Successfully
        if mf_command_result == 0:
            user_id = create_new_user(user_id=user_id, username=username, domain=domain)
            
            # MediaFlux upload result counts
            db_upload = db_create_problem(user_id, prob_full_name, prob_abbr, prob_type_id, prob_instance_suffix)
            if db_upload:
                show_success(f"'{prob_full_name}: {prob_abbr}' problem has been created successfully!")
                return user_id, prob_abbr
        else:
            show_error(f"Failed to create '{prob_full_name}'. ")
    except KeyboardInterrupt:
        show_exit()
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error: {e}")
        show_error("An unexpected error has occurred. Please try again.")
        sys.exit(1)
    finally:
        mf_clean_up(tmp_dir=True, log_dir=True)


if __name__ == "__main__":
    create_problem()
