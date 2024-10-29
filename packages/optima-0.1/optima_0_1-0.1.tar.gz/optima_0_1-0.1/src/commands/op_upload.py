from typing import Optional
import sys

from services.db_services import db_create_or_update_instances, db_update_metadata, db_update_readme
from services.mf_utils import update_mf_config_file
from config import get_logger

logger = get_logger(__name__)

from constants import FileType
from commands.op_create import create_problem
from commands.op_utils import create_new_user, get_or_prompt_user_info
from services.cli_handler import *
from services.cli_messages import show_error, show_success, show_exit, show_splitter
from services.mf_upload import *
from services.mf_utils import mf_clean_up, mf_read_operation_log


def upload(
    username: Optional[str] = None,
    problem_abbr_name: Optional[str] = None,
    file_type: Optional[FileType] = None,
    file_path: Optional[str] = None,
) -> None:
    """Main function to handle file uploads and perform upload instance operations."""
    try:
        # Step 1: User
        user_id, username, domain = get_or_prompt_user_info(username)

        # Step 2: Problem
        prob_abbr = select_problem(problem_abbr_name)
        if prob_abbr == "Create New Problem":
            user_id, prob_abbr = create_problem(username=username, domain=domain)
        
        prob_data = fetch_problem_by_abbr(prob_abbr)    
        prob_id, instance_suffix = prob_data.get("id"), prob_data.get("instance_suffix")

        # Step 3: Upload FileType
        file_type = file_type or select_upload_file_type()

        update_mf_config_file(username=username, domain=domain)

        # Step 4: Local Dir/File Path to Upload according to type, and build MF execution command
        # 1. INSTANCES
        if file_type == FileType.INSTANCE:
            # Classify instance categories and handle mismatched category (if only one category)
            src_path = prompt_for_instances_path(file_path=file_path, instance_suffix=instance_suffix)
            categorized_instances, new_categories = classify_instance_category(src_path, prob_id)
            if len(categorized_instances) == 1 and new_categories:
                categorized_instances = select_mismatched_category_action(
                    list(new_categories)[0], categorized_instances
                )
            src_path = copy_instances_to_tmp(categorized_instances)
            mf_command = build_mf_upload_command(mf_dest_path=f"{prob_abbr}", src_path=src_path)

        # 2. README
        elif file_type == FileType.README:
            src_path = prompt_for_single_upload_path(file_path=file_path, required_suffix="md")
            mf_command = build_mf_upload_command(mf_dest_path=f"{prob_abbr}", src_path=src_path)

        # 3. METADATA
        elif file_type == FileType.METADATA:
            src_path = prompt_for_single_upload_path(file_path=file_path, required_suffix="csv")
            mf_command = build_mf_upload_command(mf_dest_path=f"{prob_abbr}", src_path=src_path)

        # Step 5: Execute MF command
        show_splitter()
        mf_command_result = os.system(mf_command)
        show_splitter()
        
        # MediaFlux Command Executed Successfully
        if mf_command_result == 0:
            user_id = create_new_user(user_id=user_id, username=username, domain=domain)
            
            # MediaFlux upload result counts
            log_content = mf_read_operation_log()
            mf_upload, mf_skip, mf_fail = parse_mf_upload_counts(log_content).values()
                        
            if mf_upload == 0 and mf_skip > 0:
                show_success(f"No uploads: {mf_skip} identical {file_type.value} files skipped.")
            
            elif mf_upload > 0: 
                if file_type == FileType.INSTANCE:
                    mf_uploaded_files = parse_mf_uploaded_files(log_content)
                    categorized_instances = filter_mf_uploaded_files(categorized_instances, mf_uploaded_files)
                    db_upload = db_create_or_update_instances(user_id, prob_id, categorized_instances)
                    if db_upload == mf_upload: 
                        show_success(f"Uploaded {mf_upload} {file_type.value} files and skipped {mf_skip} identical files.")
                elif file_type == FileType.README:
                    db_upload = db_update_readme(prob_id, src_path)
                    if db_upload:
                        show_success(f"README file has been uploaded successfully!")
                elif file_type == FileType.METADATA:
                    db_upload = db_update_metadata(prob_id, src_path)
                    if db_upload:
                        show_success(f"Metadata file has been uploaded successfully!")
        else:
            show_error("Upload failed.")
    except KeyboardInterrupt:
        show_exit()
        sys.exit(1)
    except Exception as e:
        logger.error(e)
        show_error("An unexpected error has occurred. Please try again.")
        sys.exit(1)
    finally:
        mf_clean_up(tmp_dir=True, log_dir=True)


if __name__ == "__main__":
    upload()
