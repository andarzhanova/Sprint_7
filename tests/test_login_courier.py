import pytest
import requests
import allure
import helpers
from constants import Constants


@allure.feature('Логин курьера')
class TestLoginCourier:
    @allure.title('Проверка возврата "id" при успешной авторизации курьера')
    @allure.description(
        'Отправляем запрос, который авторизует курьера и проверяем, '
        'что вернулся ожидаемый код и "id" в тексте ответа'
    )
    def test_login_courier_success(self, registered_courier):
        payload = registered_courier
        response = requests.post(Constants.LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Проверка ошибки при авторизации с неверным логином или паролем')
    @allure.description(
        'Отправляем запрос, который авторизует курьера, с неверным логином или паролем и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    @pytest.mark.parametrize('field', ["login", "password"])
    def test_login_courier_with_invalid_log_or_pass(self, registered_courier, field):
        payload = registered_courier.copy()
        payload[field] += 'invalid'
        response = requests.post(Constants.LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and response.text == '{"message": "Учетная запись не найдена"}'

    @allure.title('Проверка ошибки при авторизации без поля логина или пароля')
    @allure.description(
        'Отправляем запрос, который авторизует курьера, без поля логина или пароля и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    @pytest.mark.parametrize('field', ["login", "password"])
    def test_login_courier_no_login_or_no_pass_field(self, registered_courier, field):
        payload = registered_courier.copy()
        del payload[field]
        response = requests.post(Constants.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and response.text == '{"message": "Недостаточно данных для входа"}'

    @allure.title('Проверка ошибки при авторизации под несуществующим пользователем')
    @allure.description(
        'Отправляем запрос, который авторизует курьера под несуществующим пользователем, и проверяем, '
        'что вернулись ожидаемые код и текст ответа об ошибке'
    )
    def test_login_unregistered_courier(self):
        login, password, firstname = helpers.generate_login_pass()
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Constants.LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and response.text == '{"message": "Учетная запись не найдена"}'
