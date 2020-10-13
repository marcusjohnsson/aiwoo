import pickle

def save_customers_on_file(customers):
    with open('customers.pkl', 'wb') as f:
        pickle.dump(customers, f)

def load_customers_on_file():
    with open('customers.pkl', 'rb') as f:
        customers_on_file = pickle.load(f)
        return customers_on_file

