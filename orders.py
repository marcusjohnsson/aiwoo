from aiwoo_api import *

class Order:
    def __init__(self, id, date_created, total, status, customer, shipping, line_items, weight=0):
        self.id = id
        self.date_created = date_created
        self.total = total
        self.status = status
        self.customer = customer
        self.shipping = shipping
        self.line_items = line_items
        self.weight = weight


def determine_shipping_weight(line_items):
    return 'undetermined'
    # find a way to compute minimum shipping weight:
    # 250g, 500g, 1000g or 2000g


def get_orders(status):
    orders_dump = fetch_all_orders(status)
    orders = []
    for o in orders_dump:
        orders.append(
            Order(
                id = o['id'],
                date_created = o['date_created'],
                total = o['total'],
                status = o['status'],
                customer = {
                        'id': o['customer_id'],
                        'first_name': o['billing']['first_name'],
                        'last_name': o['billing']['first_name'],
                        'email': o['billing']['email'],
                        'phone': o['billing']['phone']
                    },
                shipping = {
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
                line_items = o['line_items'],
                weight = determine_shipping_weight(o['line_items'])
            )
        )

    return orders
