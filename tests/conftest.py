import pytest
import json


@pytest.fixture()
def data(file_path='../ls-command/files/structure.json'):
    file = open(file_path)
    data = json.load(file)
    file.close()
    return data
