from config import *
from woocommerce import API
# DOCS: https://woocommerce.github.io/woocommerce-rest-api-docs/?python#introduction

wcapi = API(
    url=URL,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    version=VERSION
)

def customers(data={"per page": 100}):
    res = wcapi.get("customers/", params=data).json()  # per_page 100 seem to be max orders returned.
    return res

def order(id):
    res = wcapi.get("orders/" + str(id)).json()
    return res


def orders(data=None):
    if data is None:
        data = {"per page": 100}
    res = wcapi.get("orders/", params=data).json()
    return res


def product(id):
    res = wcapi.get("products/" + str(id)).json()
    return res


def products():
    res = wcapi.get("products/?per_page=100").json()
    return res
