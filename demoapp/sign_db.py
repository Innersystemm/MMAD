from demoapp.models import SignsVector


class SignDB:
    @staticmethod
    def load_signs():
        return SignsVector.objects.all()

    @staticmethod
    def add_user(user_id, signs):
        if not SignDB.is_user_exists(user_id):
            for sign in signs:
                SignsVector(userID=user_id, sign1=sign[0], sign2=sign[1], sign3=sign[2], sign4=sign[3]).save()
            return True, 'Регистрация прошла успешно'
        return False, 'Пользователь с id: {0} уже существует'.format(user_id)

    @staticmethod
    def is_user_exists(user_id):
        users = [usr.user() for usr in SignDB.load_signs()]
        return user_id in users
