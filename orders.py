from aiwoo_api import *


class Order:
    def __init__(self, id, date_created, total, status, customer, shipping, products, weight=0):
        self.id = id
        self.date_created = date_created
        self.total = total
        self.status = status
        self.customer = customer
        self.shipping = shipping
        self.products = products
        self.weight = weight


def determine_shipping_weight(products):
    print("Determing shipping weight tier for order")
    total_weight = 0
    for item in products:
        sku_w = item['sku'][-3:]
        if item['subtotal'] == "0.00":
            pass
        else:
            if sku_w == "100":
                total_weight += int(sku_w) * int(item['quantity'])
            elif sku_w == "300":
                total_weight += int(sku_w) * item['quantity']
            elif sku_w == "500":
                total_weight += int(sku_w) * item['quantity']
            else:
                total_weight += 50 * item['quantity']

    freight = 0
    ## Below 250
    if total_weight <= 250:
        freight = 250
    ## Below 500
    if 250 <= total_weight <= 500:
        freight = 500
    ## Below 1000
    if 500 <= total_weight <= 1000:
        freight = 1000
    ## Below 2000
    if 1000 <= total_weight <= 2000:
        freight = 2000

    if freight == 0:
        print('freight is impossibly 0, something went wrong')
    else:
        print(f'total_weight for products is {total_weight}g => freight {freight}g')
    total_weight = 0

    return freight


def get_orders(status) -> object:
    """
    Fetches orders, initates order objects and return them as a list
    :param status: string options are pending, processing, on-hold, completed, cancelled, refunded, failed and trash
    :return List
    """
    orders_dump = fetch_all_orders(status)
    orders = []
    for o in orders_dump:
        orders.append(
            Order(
                id=o['id'],
                date_created=o['date_created'],
                total=o['total'],
                status=o['status'],
                customer={
                    'id': o['customer_id'],
                    'first_name': o['billing']['first_name'],
                    'last_name': o['billing']['last_name'],
                    'email': o['billing']['email'],
                    'phone': o['billing']['phone']
                },
                shipping={
                    'first_name': o['shipping']['first_name'],
                    'last_name': o['shipping']['last_name'],
                    'company': o['shipping']['company'],
                    'address_1': o['shipping']['address_1'],
                    'address_2': o['shipping']['address_2'],
                    'postcode': o['shipping']['postcode'],
                    'city': o['shipping']['city'],
                    'state': o['shipping']['state'],
                    'country': o['shipping']['country'],
                },
                products=o['line_items'],
                weight=determine_shipping_weight(o['line_items'])
            )
        )

    return orders
