import json
import requests
from jsonschema import validate
from utils import resource


def validator_all_json_scheme(name, url):
    response = requests.get(url=url)
    schema = json.load(open(resource.path_json_scheme(file_name=name)))
    validate(response.json(), schema)
