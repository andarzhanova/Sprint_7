import requests
import allure


@allure.feature('Список заказов')
class TestOrderList:
    @allure.title('Проверка возврата списка заказов в тело ответа')
    @allure.description(
        'Отправляем запрос, который получает список заказов и проверяем, '
        'что в тело ответа вернулся список заказов'
    )
    def test_order_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert "orders" in response.json() and type(response.json()["orders"]) is list
