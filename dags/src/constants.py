from dotenv import load_dotenv
from os import getenv
from io_utils import add_cwd_to_file_path

load_dotenv()
FILE_PATH = add_cwd_to_file_path(getenv("FILE_PATH"))