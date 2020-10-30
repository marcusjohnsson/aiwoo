from config import *
from woocommerce import API

# DOCS: https://woocommerce.github.io/woocommerce-rest-api-docs/?python#introduction

wcapi = API(
    url=URL,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    version=VERSION
)


# Fetch all orders from server
# status options: pending, processing, on-hold, completed, cancelled, refunded, failed and trash. Default is pending.
def fetch_all_orders(status):
    print(f"Fetching all {status} orders...")
    all_orders = []
    fetching = True
    data = {
        "page": 1,
        "per_page": 100,
        "status": status
    }

    while fetching:
        if len(wcapi.get("orders/", params=data).json()) == 0:
            print(f'Fetching complete: {len(all_orders)} {status} orders acquired')
            all_orders_sorted = sorted(all_orders, key=lambda k: k['id'])
            return all_orders_sorted
        else:
            for c in wcapi.get("orders/", params=data).json():
                all_orders.append(c)

            print(f'Page @ {data["page"]} | {len(all_orders)}')
            data['page'] += 1


# Fetch all customers from server
# Broken, only returns some of the customers, not all.
def fetch_all_customers():
    print("Fetching all customers...")
    all_customers = []
    fetching = True
    data = {
        "page": 1,
        "per_page": 100
    }

    while fetching:
        if len(wcapi.get("customers/", params=data).json()) == 0:
            print(f'Fetching complete: {len(all_customers)} customers acquired')
            all_customers_sorted = sorted(all_customers, key=lambda k: k['first_name'])
            return all_customers_sorted
        else:
            for c in wcapi.get("customers/", params=data).json():
                all_customers.append(c)
        print(f'Page @ {data["page"]} | {len(all_customers)} acquired')
        data['page'] += 1


# Checks if customer is a former member.
# Broken, since fetch_all_customers() is broken it does run reliably, yields false positive.
def is_member(str):
    data = {"search": str}
    res = wcapi.get("customers/", params=data).json()
    if len(res) == 0:
        return False
    else:
        return True


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
