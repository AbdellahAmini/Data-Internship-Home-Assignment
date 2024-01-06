import os

def write_txt(
    file_path: str,
    txt_content: str,
    encoding: str = "utf-8"
) -> None:
    """
    Writes a .txt file at the provided filepath.
    
    Args:
        file_path: where to write the file
        txt_content: the string object to write
        encoding: which encoding to use when writing the file, default is utf-8

    Returns:
        None
    """
    with open(file=file_path, mode="w", encoding=encoding) as f:
        f.write(txt_content)

def add_cwd_to_file_path(
    file_path: str
) -> str:
    """
    Constructs a file's full path by joining the file_path to the current working directory.
    
    Example:
        - current working directory: C\\Users\\user\\Desktop
        - file path: foder_name\\sub_folder_name\\file_name
        => full path: C\\Users\\user\\Desktop\\foder_name\\sub_folder_name\\file_name

    Args:
        file_path: the path of the file
    
    Returns:
        the concatinated file path
    """
    return os.path.join(
        os.getcwd(),
        file_path
    )