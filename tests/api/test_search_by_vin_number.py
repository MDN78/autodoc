import os
import allure
from allure_commons.types import Severity
from autodoc_project.data.cars import Car
from autodoc_project.api.board_api import board_api

@allure.tag('API')
@allure.story('Search item by WIN number via API')
@allure.title('Search item by WIN number')
@allure.severity(Severity.NORMAL)
@allure.feature('Search check')
@allure.link('https://www.autodoc.ru/', name='Autodoc.ru')
def test_search_by_vin_number():
    token = board_api.get_auth_token()
    car = Car(
        manufacturer=os.getenv('CAR_MANUFACTURER'),
        model=os.getenv('CAR_MODEL'),
        vin=os.getenv('VIN_NUMBER')
    )
    car_info = board_api.search_by_vin_number(car.vin, token)

    assert car_info[0] == car.manufacturer
    assert car_info[1] == car.model
