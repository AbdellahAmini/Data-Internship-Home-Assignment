from dotenv import load_dotenv
from os import getenv
from io_utils import add_cwd_to_file_path

# envrionment variables
load_dotenv()
FILE_PATH = add_cwd_to_file_path(getenv("FILE_PATH"))

OUTPUT_DIR_EXTRACTED = add_cwd_to_file_path(getenv("OUTPUT_DIR_EXTRACTED"))
OUTPUT_DIR_TRANSFORMED = add_cwd_to_file_path(getenv("OUTPUT_DIR_TRANSFORMED"))
DB_PATH = add_cwd_to_file_path(getenv("DB_PATH"))
