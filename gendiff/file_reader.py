from pathlib import Path
from gendiff.parser_logic import load_file_data


def get_file_data(path_to_file):
    format = get_extention(path_to_file)
    file_data = load_file_data(open_file(path_to_file), format)
    return file_data


def get_extention(path_to_file):
    extention = Path(path_to_file).suffix
    if extention.lower() == '.json':
        return 'json'
    elif extention == '.yaml':
        return 'yaml'
    elif extention == '.yml':
        return 'yml'


def open_file(filename):
    return open(filename)
