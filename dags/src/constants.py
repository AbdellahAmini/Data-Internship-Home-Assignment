from dotenv import load_dotenv
from os import getenv
from src.io_utils import add_cwd_to_file_path

# envrionment variables
# load_dotenv()
FILE_PATH="source/jobs.csv"
FILE_PATH = add_cwd_to_file_path(FILE_PATH)

OUTPUT_DIR_EXTRACTED="staging\extracted\context_data"
OUTPUT_DIR_EXTRACTED = add_cwd_to_file_path(OUTPUT_DIR_EXTRACTED)

OUTPUT_DIR_TRANSFORMED="staging\transformed\transformed_data"
OUTPUT_DIR_TRANSFORMED = add_cwd_to_file_path(OUTPUT_DIR_TRANSFORMED)

DB_PATH="my_database.db"
DB_PATH = add_cwd_to_file_path(DB_PATH)