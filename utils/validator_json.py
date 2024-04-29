import json
import allure
import requests
from utils import resource
from utils.logger import step
from jsonschema import validate


@step
@allure.step('API: validate JSON scheme')
def validator_all_json_scheme(name, url):
    with allure.step('Get request'):
        response = requests.get(url=url)
    with allure.step('Get JSON scheme'):
        schema = json.load(open(resource.path_json_scheme(file_name=name)))
    with allure.step('Validate scheme'):
        validate(response.json(), schema)
