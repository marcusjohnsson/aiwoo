from aiwoo_api import *
from config import *
import pickle


# Fetch all customers from server
def fetch_all_customers():
    print("Fetching all customers...")
    all_customers = []
    fetching = True
    data = {
        "page": 1,
        "per_page": 100
    }

    while fetching:
        if len(customers(data)) == 0:
            print(f'Fetching complete: {len(all_customers)} customers acquired')
            all_customers_sorted = sorted(all_customers, key=lambda k: k['first_name'])
            return all_customers_sorted
        else:
            for c in customers(data):
                all_customers.append(c)
        print(f'Page @ {data["page"]} | {len(all_customers)} acquired')
        data['page'] += 1


# Fetch all orders from server
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
        if len(orders(data)) == 0:
            print(f'Fetching complete: {len(all_orders)} {status} orders acquired')
            all_orders_sorted = sorted(all_orders, key=lambda k: k['id'])
            return all_orders_sorted
        else:
            for c in orders(data):
                all_orders.append(c)

            print(f'Page @ {data["page"]} | {len(all_orders)}')
            data['page'] += 1



def save_customers_on_file(customers):
    with open('customers.pkl', 'wb') as f:
        pickle.dump(customers, f)


def load_customers_on_file():
    with open('customers.pkl', 'rb') as f:
        customers_on_file = pickle.load(f)
        return customers_on_file


def is_member(str):
    data = {"search": str}
    res = wcapi.get("customers/", params=data).json()
    if len(res) == 0:
        return False
    else:
        return True


def main():
    # print all orders until orders() lenght is 0.
    # save  orders to dat file

    # print(len(orders(data)))
    # for ord in orders(data):
    #     print(f'{ord["id"]} - Created {ord["date_created"]} - Order Value - {ord["total"]}')
    #
    # print(order(2))

    # allcusts = fetch_all_customers()
    # for cust in allcusts:
    #     print(cust)
    #save_customers_on_file(allCusts)

    # custs = load_customers_on_file()
    # for c in custs:
    #      print(f"{c['id']} {c['first_name']} {c['last_name']} {c['email']}")
         # print(f'is member {is_member(c["email"])}')

    # email = "jonasolsone@hotmail.com"
    # print(is_member(email))
    customers = fetch_all_customers()
    print([cust['id'] for cust in customers])

if __name__ == '__main__':
    main()



