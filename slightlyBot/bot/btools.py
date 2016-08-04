import pickle
import os


def check_folder(folder):
    path = os.path.abspath(__file__)
    dirpath = os.path.join(os.path.dirname(path), folder)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath


def sflow(args, folder='logs'):
    dirpath = check_folder(folder)
    for obj, fn in args:
        fn = os.path.join(dirpath, fn)
        pickle.dump(obj, open(fn, 'w'))


def gflow(fn, folder='logs'):
    dirpath = check_folder(folder)
    file = open(os.path.join(dirpath, fn))
    return pickle.load(file)
