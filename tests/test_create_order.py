import pytest
import requests
import allure
from constants import Constants


@allure.feature('Создание заказа')
class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа при разном заполнении поля "цвет"')
    @allure.description(
        'Отправляем запрос, который создаёт заказ с разным заполнением поля "цвет" и проверяем, '
        'что вернулся ожидаемый код и текст ответа об успешном создании содержит track'
    )
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        response = requests.post(Constants.ORDER, params=payload)
        assert response.status_code == 201 and "track" in response.text
