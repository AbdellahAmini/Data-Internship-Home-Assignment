import io_utils as my_io

from processing_utils import transform_data
from constants import OUTPUT_DIR_EXTRACTED, OUTPUT_DIR_TRANSFORMED

def transform_data():
        # Sort files in the directory OUTPUT_DIR_EXTRACTED using a natural sorting key
        files = my_io.list_files_sorted(OUTPUT_DIR_EXTRACTED)

        my_io.create_file_dir(OUTPUT_DIR_TRANSFORMED)
        files_len = len(files)
        print(f"Transforming {files_len} files")

        # Process each file in the sorted list
        for i, file_name in enumerate(files):
                # Construct the full path for each file
                input_dir = f"{OUTPUT_DIR_EXTRACTED}/{file_name}"

                # Read the JSON content from the file
                data = my_io.read_json(input_dir)

                # Transform the data using the transform_data function
                # and write the transformed data to a new JSON file
                my_io.write_json(f"{OUTPUT_DIR_TRANSFORMED}/output{i}.json", transform_data(data))
                if i > 0 and i % 100 == 0:
                        print(f"Transformed {i+1}/{files_len} files")
