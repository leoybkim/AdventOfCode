from pathlib import Path


def read_file(relative_file_path: str, file_reference=None) -> str:
    """
    Reads a file using a path relative to the calling script's location

    :param relative_file_path: path to the file relative to the caller
    :param file_reference: __file__ variable from the caller
    :return: file data
    """
    if file_reference:
        full_file_path = get_base_path(file_reference) / Path(relative_file_path)
    else:
        full_file_path = relative_file_path

    with open(full_file_path) as input_file:
        return input_file.read()


def get_base_path(file_reference: str) -> Path:
    return Path(file_reference).resolve().parent
