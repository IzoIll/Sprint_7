class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    POST_COURIER = f'{BASE_URL}api/v1/courier'
    DELETE_COURIER = f'{BASE_URL}api/v1/courier/:id'
    LOGIN_COURIER = f'{BASE_URL}api/v1/courier/login'
    CREATE_ORDER = f'{BASE_URL}api/v1/orders'