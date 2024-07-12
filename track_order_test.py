import data
import sender_stand_reqest
# Юлия Голосникова, 18-я Кагорта - Финальный проект. Инженер по тестированию расширенный


# запрос на получение заказа по треку заказа
def get_order_track_status_code():
    response_code =sender_stand_reqest.post_order(data.order_body)
    track = response_code.json()["track"]
    return sender_stand_reqest.get_order_track(track).status_code

# Проверка, что код ответа равен 200.
def test_get_order_track_code_200():
    assert get_order_track_status_code() == 200