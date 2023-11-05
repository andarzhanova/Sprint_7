import pytest
import requests
import helpers


@pytest.fixture
def unregistered_courier():
    login, password, firstname = helpers.generate_login_pass()
    payload = {
        "login": login,
        "password": password,
        "firstName": firstname
    }

    yield payload
    del payload["firstName"]
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')


@pytest.fixture
def registered_courier():
    login, password, firstname = helpers.register_new_courier_and_return_login_password()
    payload = {
        "login": login,
        "password": password
    }

    yield payload
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')
