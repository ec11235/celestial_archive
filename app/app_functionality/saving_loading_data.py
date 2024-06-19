import pickle
import os

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_from_pickle(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'rb') as f:
        try:
            return pickle.load(f)
        except (pickle.UnpicklingError, EOFError):
            return {}