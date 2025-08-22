import requests
import allure

from helper import *
from data import *

@allure.description('Проверка ручки "Логин курьера в системе"')
class TestCheckLoginCourier:
    @allure.title('Вход в систему с существующими данными')
    def test_registration_and_login_courier(self, new_courier):
        with allure.step(f"Отправляем запрос на логин курьера"):
            response = requests.post(Urls.LOGIN_COURIER, data=new_courier)
        assert response.json() == {'id': response.json()['id']}
        assert response.status_code == Answers.SUCCESS_LOGIN_COURIER['code']

    @allure.title('Вход в систему с несуществующим логином и паролем')
    def test_login_without_registration_courier(self):
        random_courier = generate_courier()
        with allure.step(f"Отправляем запрос на логин курьера"):
            response = requests.post(Urls.LOGIN_COURIER, data=random_courier)
        assert response.json()['message'] == Answers.NOT_FOUND['message']
        assert response.status_code == Answers.NOT_FOUND['code']

    @allure.title('Вход в систему без ввода логина')
    def test_login_without_registration_and_login_courier(self):
        random_courier = generate_courier_without_login()
        with allure.step(f"Отправляем запрос на логин курьера"):
            response = requests.post(Urls.LOGIN_COURIER, data=random_courier)
        assert response.json()['message'] == Answers.NOT_ENOUGH_DATA_LOGIN['message']
        assert response.status_code == Answers.NOT_ENOUGH_DATA_LOGIN['code']

    @allure.title('Вход в систему без ввода пароля')
    def test_login_without_registration_and_password_courier(self):
        random_courier = generate_courier_without_password()
        with allure.step(f"Отправляем запрос на логин курьера"):
            response = requests.post(Urls.LOGIN_COURIER, data=random_courier)
        assert response.json()['message'] == Answers.NOT_ENOUGH_DATA_LOGIN['message']
        assert response.status_code == Answers.NOT_ENOUGH_DATA_LOGIN['code']