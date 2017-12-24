import string

from demoapp.sign_db import SignDB


class SignValidator:
    @staticmethod
    def is_sign_valid(signs, sign_len=4):
        for sign in signs:
            if len(sign.split(' ')) != sign_len:
                return False, 'Размер вектора признаков != {0}, текущий размер: {1}'.format(sign_len,
                                                                                            len(sign.split(' ')))
            if any([char in string.ascii_letters for char in sign]):
                return False, 'Вектор признаков не должен содержать букв'
        return True, 'Вектор признаков корректный'

    @staticmethod
    def check_user(user_id, signs):
        status, msg = SignValidator.is_sign_valid(signs)
        if status is False:
            return False, msg
        # Берем данные из бд

        if SignDB.is_user_exists(user_id):
            return False, 'Пользователь не найден'

        return True, 'ОК'
