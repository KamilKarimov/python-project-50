# Logic of generating difference

from gendiff.formatters.formatter import choose_format

from .parser_logic import get_file_data
from .generate_dict_diff import make_diff


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = get_file_data(file_path1)
    file2 = get_file_data(file_path2)
    diff = make_diff(file1, file2)
    return choose_format(diff, format)
