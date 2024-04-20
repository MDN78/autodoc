import requests
import os
from dotenv import load_dotenv
from autodoc_project.data.users import User

load_dotenv()


class BoardApi():

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
        # print(status_code)
        # print(response.text)
        # print(my_token)

        url = 'https://webapi.autodoc.ru/api/client/profile'
        param = {
            'withUpdate': True
        }
        head = {
            'authorization': f'Bearer {my_token}'
        }
        auth = requests.get(url=url, params=param, headers=head)
        print(auth.text)

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

    def clear_cart(self, my_token):
        payload = {}
        head = {
            'authorization': f'Bearer {my_token}'
        }
        url = "https://webapi.autodoc.ru/api/shoppingcart/items/"
        response = requests.delete(url, headers=head, data=payload)
        status_code = response.status_code
        assert status_code == 204

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


board_api = BoardApi()
