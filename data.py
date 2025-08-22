class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    POST_COURIER = f'{BASE_URL}api/v1/courier'
    DELETE_COURIER = f'{BASE_URL}api/v1/courier/:id'
    LOGIN_COURIER = f'{BASE_URL}api/v1/courier/login'
    CREATE_ORDER = f'{BASE_URL}api/v1/orders'

class Answers:

    SUCCESS_REGISTRATION_COURIER = {'code': 201, 'ok': 'true'}
    NOT_ENOUGH_DATA_REGISTRATION = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    LOGIN_IS_TAKEN = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    SUCCESS_LOGIN_COURIER = {'code': 200}
    NOT_ENOUGH_DATA_LOGIN = {'code': 400, 'message': 'Недостаточно данных для входа'}
    NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}

    SUCCESS_CREATE_ORDER = {'code': 201}
    SUCCESS_GET_ORDER_LIST = {'code': 200}