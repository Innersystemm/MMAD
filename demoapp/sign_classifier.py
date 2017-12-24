import math

import numpy as np
from demoapp.sign_db import SignDB
from demoapp.sign_validator import SignValidator


class Sign:
    @staticmethod
    def to_numeric_array(sign_str):
        return np.array([int(sign) for sign in sign_str.split(' ')])

    @staticmethod
    def cast_data_to_numeric_val(user_id, signs):
        return int(user_id), [Sign.to_numeric_array(sg) for sg in signs]

    @staticmethod
    def process_sign(user_id, sign, k=2):
        status, msg = SignValidator.check_user(user_id, [sign])
        if status is False:
            return status, 'Ошибка: {0}'.format(msg)

        db_data = np.array([sg.vector() for sg in SignDB.load_signs()])

        proceed_sign = Sign.to_numeric_array(sign)
        object_class = Sign.k_nearest(db_data, k, proceed_sign)
        if object_class == int(user_id):
            return True, 'Аторизация успеша. Распознан пользователь с ID: {0}'.format(object_class)
        else:
            return False, 'Неверный id пользователя/вектор признаков'

    @staticmethod
    def k_nearest(X, k, obj):
        sub_X = X[:, 0:-1]
        m = np.mean(sub_X, axis=0)
        s = np.std(sub_X, axis=0)
        sub_X = (sub_X - m) / s
        obj = (obj - m) / s
        distances = np.array([Sign.dist(obj, x) for x in sub_X])
        distances = np.argsort(distances)
        nearest_classes = np.array(X[distances[:k], -1])
        unique, counts = np.unique(nearest_classes, return_counts=True)
        object_class = unique[np.argmax(counts)]
        return object_class

    @staticmethod
    def dist(p1, p2):
        return math.sqrt(sum((p1 - p2) ** 2))
