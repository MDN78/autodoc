import os

import allure
import requests
from utils.logger import step
from dotenv import load_dotenv
from autodoc_project.data.users import User

load_dotenv()


class BoardApi():

    @step
    @allure.step('API: get auth token')
    def get_auth_token(self):
        payload = {
            'username': os.getenv('USER_LOGIN'),
            'password': os.getenv('USER_PASSWORD'),
            'grant_type': 'password'
        }
        headers = {
            'authorization': 'Bearer',
            'content-type': 'application/x-www-form-urlencoded',
        }
        response = requests.post('https://auth.autodoc.ru/token', data=payload, headers=headers)
        my_token = response.json()['access_token']
        return my_token

    @step
    @allure.step('API: authorization user via API')
    def authorization_user(self, user: User):
        payload = {
            'username': user.username,
            'password': user.password,
            'grant_type': 'password'
        }
        headers = {
            'authorization': 'Bearer',
            'content-type': 'application/x-www-form-urlencoded',
        }
        response = requests.post('https://auth.autodoc.ru/token', data=payload, headers=headers)
        my_token = response.json()['access_token']
        status_code = response.status_code
        assert status_code == 200

        url = 'https://webapi.autodoc.ru/api/client/profile'
        param = {
            'withUpdate': True
        }
        head = {
            'authorization': f'Bearer {my_token}'
        }
        auth = requests.get(url=url, params=param, headers=head)

    @step
    @allure.step('API: Add item to cart')
    def add_item_to_cart(self, item, number, my_token):
        url = 'https://webapi.autodoc.ru/api/shoppingcart/items'

        head = {
            'authorization': f'Bearer {my_token}'
        }

        payload = {
            "directionToManufacturerId": 0,
            "quantity": 1,
            "quantityInPart": 1,
            "price": 996,
            "priceId": 611077508,
            "clientPartName": "Жидкость ГУР",
            "partNumber": number,
            "pricePartName": "Жидкость ГУР",
            "supplierName": "SPA117*",
            "manufacturerId": 5703,
            "manufacturerName": item,
            "quantityInStore": 40,
            "description": "",
            "deliveryDays": 0,
            "idPartner": 12560,
            "priceType": 1
        }
        response = requests.post(url, headers=head, data=payload)
        status_code = response.status_code
        assert status_code == 204

    @step
    @allure.step('API: Clear cart')
    def clear_cart(self, my_token):
        payload = {}
        head = {
            'authorization': f'Bearer {my_token}'
        }
        url = "https://webapi.autodoc.ru/api/shoppingcart/items/"
        response = requests.delete(url, headers=head, data=payload)
        status_code = response.status_code
        assert status_code == 204

    @step
    @allure.step('API: Search by vin number')
    def search_by_vin_number(self, vin, my_token):
        url = f'https://catalogoriginal.autodoc.ru/api/catalogs/original/cars/{vin}/modifications'
        payload = {}
        head = {
            'authorization': f'Bearer {my_token}'
        }
        response = requests.get(url=url, headers=head, data=payload)
        status_code = response.status_code
        assert status_code == 200
        manufacturer = response.json()["commonAttributes"][2]['value']
        model = response.json()["commonAttributes"][6]['value']
        return [manufacturer, model]

    @step
    @allure.step('API: Search by title and number')
    def search_by_title_and_number(self, name, number):
        url = f"https://webapi.autodoc.ru/api/manufacturers/{name}{number}"
        param = {
            'showAll': False
        }
        response = requests.get(url, params=param)
        manufacturer = response.json()[0]['manufacturerName']
        artnumber = response.json()[0]['artNumber']

        return [manufacturer, artnumber]


board_api = BoardApi()
