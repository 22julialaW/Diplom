import requests
import configuration
import data

# Юлия Голосникова, 18-я Кагорта - Финальный проект. Инженер по тестированию расширенный
def post_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=data.headers,
                         json=data.order_body)


def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER + '?t=' + str(track),
                        headers=data.headers)
# запрос на получение заказа по треку заказа
def get_order_track_status_code():
    response_code = post_order(data.order_body)
    track = response_code.json()["track"]
    return get_order_track(track).status_code

# Проверка, что код ответа равен 200.
def test_get_order_track_code_200():
    assert get_order_track_status_code() == 200