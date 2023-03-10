import json
import yaml


def load_file_data(filename, format):
    if format == 'json':
        return json.load(filename)
    elif format == 'yaml' or format == 'yml':
        return yaml.safe_load(filename)
