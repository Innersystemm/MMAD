import numpy as np
import string as string
import math

sign_length = 4


def load_signs(path='demoapp/signs.txt'):
    data = open(path).readlines()
    return matrix(data)


def is_sign_valid(sign, sign_len=sign_length):
    if len(sign.split(' ')) != sign_len:
        return False
    return False if any([char in string.ascii_letters for char in sign]) else True


def process_sign(sign):
    return np.array([int(str) for str in sign.split(' ')])


def check_sign(sign, user_id):
    if not is_sign_valid(sign):
        return False
    signs = load_signs()
    users = signs[:, -1]
    if int(user_id) not in users:
        return 'User not found'
    proceed_sign = process_sign(sign)
    k = 2
    object_class = k_nearest(signs, k, proceed_sign)
    # 1 - Auth success, 0 - Auth fail
    auth_state = {1: True, 0: False}
    return auth_state[object_class]


def k_nearest(X, k, obj):
    sub_X = X[:, 0:-1]
    m = np.mean(sub_X, axis=0)
    s = np.std(sub_X, axis=0)
    sub_X = (sub_X - m) / s
    obj = (obj - m) / s
    distances = np.array([dist(obj, x) for x in sub_X])
    distances = np.argsort(distances)
    nearest_classes = np.array(X[distances[:k], -1])
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]
    return object_class


def dist(p1, p2):
    return math.sqrt(sum((p1 - p2) ** 2))


def matrix(matr):
    return np.array([[int(strv) for strv in val] for val in [_str.split() for _str in matr]])
