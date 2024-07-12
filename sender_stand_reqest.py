import requests
import configuration
import data


def post_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=data.headers,
                         json=order_body)


def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + '?t=' + str(track),
                        headers=data.headers)
