import pytest
import requests
import allure
import helpers
from constants import Constants


@allure.feature('Создание курьера')
class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description(
        'Отправляем запрос, который создаёт курьера и проверяем, '
        'что вернулись ожидаемые код и текст ответа об успешном создании'
    )
    def test_create_courier_success(self, unregistered_courier):
        payload = unregistered_courier
        response = requests.post(Constants.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка ошибки при создании одинаковых курьеров')
    @allure.description(
        'Отправляем запросы, которые создают одинаковых курьеров и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    def test_create_identical_couriers(self, unregistered_courier):
        payload = unregistered_courier
        requests.post(Constants.CREATE_COURIER, data=payload)
        response = requests.post(Constants.CREATE_COURIER, data=payload)
        assert response.status_code == 409 and response.text == '{"message":"Этот логин уже используется"}'

    @allure.title('Проверка успешного создания курьера при заполнении обязательных полей')
    @allure.description(
        'В запрос, который создаёт курьера, передаём только обязательные поля и проверяем, '
        'что вернулись ожидаемые код и текст ответа об успешном создании'
    )
    def test_create_courier_no_name_field(self, unregistered_courier):
        payload = unregistered_courier
        payload["firstName"] = None
        response = requests.post(Constants.CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка ошибки при создании курьера без обязательного поля')
    @allure.description(
        'Отправляем запрос, который создаёт курьера, без обязательного поля и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    @pytest.mark.parametrize('field', ["login", "password"])
    def test_create_courier_no_login_or_no_pass_field(self, field):
        login, password, firstname = helpers.generate_login_pass()
        payload = {
            "login": login,
            "password": password,
            "firstName": firstname
        }
        del payload[field]
        response = requests.post(Constants.CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.text == '{"message":"Недостаточно данных для ' \
                                                                'создания учетной записи"}'
