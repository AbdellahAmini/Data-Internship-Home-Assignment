import os
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from io_utils import read_json
from constants import OUTPUT_DIR_TRANSFORMED, DB_PATH

def load_data(sqlite_hook: SqliteHook):
    json_files = os.listdir(OUTPUT_DIR_TRANSFORMED)
    json_files_len = len(json_files)
    print(f"loading {json_files_len} json files")

    data_dictionary = {
        "job": [],
        "company": [],
        "education": [],
        "experience": [],
        "salary": [],
        "location": []
    }
    
    cols_dictionary = {}
    for i, file_name in enumerate(json_files):
        print(file_name)
        file_path = os.path.join(OUTPUT_DIR_TRANSFORMED, file_name)
        data = read_json(file_path)

        for k in data_dictionary.keys():
            data_dictionary[k].append(
                tuple(data[k].values())
            )

            if i == 0:
                cols_dictionary[k] = list(data[k].keys())
        
        if i > 0 and i % 100 == 0:
            print(f"loaded {i+1}/{json_files_len} files")

    
    for k in data_dictionary.keys():
        print(f"Inserting data into table {k}")
        sqlite_hook.insert_rows(table=k, rows=data_dictionary[k], target_fields=cols_dictionary[k])
    
