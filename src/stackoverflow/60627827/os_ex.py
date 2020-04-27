import os
import pickle


def pickle_wdir(filename):
    dir = os.getcwd()
    with open(filename, 'wb') as handle:
        pickle.dump(dir, handle)
