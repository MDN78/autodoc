import json
import requests
from utils import resource
from jsonschema import validate


def validator_all_json_scheme(name, url):
    response = requests.get(url=url)
    schema = json.load(open(resource.path_json_scheme(file_name=name)))
    validate(response.json(), schema)
