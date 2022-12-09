import json
from gendiff.modules.gendiff import generate_diff


def test_generate_diff():
    f1 = json.load(open('tests/fixtures/file1.json'))
    f2 = json.load(open('tests/fixtures/file2.json'))
    with open('tests/fixtures/correct_diff', mode='r') as f:
        assert generate_diff(f1, f2) == f.read()
