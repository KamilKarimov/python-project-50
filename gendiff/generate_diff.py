# Logic of generating difference

from gendiff.formatters.formatter import choose_format
from gendiff.file_reader import get_file_data


def make_diff(dict1, dict2):
    # Find difference between two dictionaries
    result = []
    keys = sorted(dict1.keys() | dict2.keys())

    for key in keys:
        node = {'name': key}
        if key not in dict1:
            node['status'] = 'added'
            node['data'] = dict2[key]
        elif key not in dict2:
            node['status'] = 'deleted'
            node['data'] = dict1[key]
        elif type(dict1[key]) is dict and type(dict2[key]) is dict:
            node['status'] = 'nested'
            node['children'] = make_diff(dict1[key], dict2[key])
        elif dict1[key] == dict2[key]:
            node['status'] = 'not changed'
            node['data'] = dict1[key]
        else:
            node['status'] = 'changed'
            node['old_value'] = dict1[key]
            node['new_value'] = dict2[key]
        result.append(node)

    return result


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = get_file_data(file_path1)
    file2 = get_file_data(file_path2)
    diff = make_diff(file1, file2)
    return choose_format(diff, format)
