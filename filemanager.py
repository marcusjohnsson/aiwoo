import pickle

def picklit(file, name):
    filename = name + '.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(file, f)

def unpicklit(file):
    filename = file + '.pkl'
    with open(filename, 'rb') as f:
        return pickle.load(f)

