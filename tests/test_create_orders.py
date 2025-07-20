import json
import allure
import pytest
import requests

from helper import *
from data import Urls

@allure.description('Проверка ручек раздела "Заказы"')
class TestCheckCreateOrders:
    @allure.description("Проверка создания заказа с указанием одного цвета, обоих цветов или без цвета")
    @pytest.mark.parametrize("colors", [["BLACK"],["GREY"],["BLACK", "GREY"],[]])
    def test_create_order(self, colors):
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва, 142 apt",
            "metroStation": 4,
            "phone": "+7 951 111 11 11",
            "rentTime": 2,
            "deliveryDate": "2025-08-01",
            "comment": "Оставьте у двери",
            "color": colors
        }
        with allure.step(f"Отправляем запрос на создание заказа с заданными параметрами цвета: {colors}"):
            response = requests.post(Urls.CREATE_ORDER, json=payload)
        with allure.step("Проверяем код ответа и тело ответа"):
            assert response.status_code == 201
            assert "track" in response.json()

    def test_get_list_order(self):
        response = requests.get(Urls.CREATE_ORDER)
        assert response.status_code == 200