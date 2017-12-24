from datetime import datetime

from demoapp.sign_classifier import Sign
from demoapp.sign_db import SignDB
from demoapp.sign_validator import SignValidator
from django.http import HttpRequest
from django.shortcuts import render

from .forms import *


def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'date': datetime.now(),
        }
    )


def auth(request):
    assert isinstance(request, HttpRequest)
    # создание экземпляра формы(django forms), содержит поля: id пользователя и строка признаков
    auth_form = AuthForm()
    status = ''
    # в этой функции выпоняется проверка, зарегистрирован ли пользователь с указанным id
    # и если таковой имеется то с помощью алгоритам knn этот пользователь классифицируется по полученному
    # вектору признаков
    # функция вовзращает true если указанный пользователь существует и полученный вектор признаков
    # успешно клссифицирован, в противно млычае возвращается false
    if 'signs' in request.POST:
        result, status = Sign.process_sign(request.POST['user_id'], request.POST['signs'])

    # Генерируем html страницу и в качестве параметров передаем форму авторизации
    # и статус текущей авторизации
    return render(
        request,
        'auth.html',
        {
            'form': auth_form,
            'status': status,
        })


def create_account(request):
    create_account_form = CreateAccountForm()
    msg = 'Введите параметры'

    if 'userId' in request.POST \
            and 'signVector1' in request.POST \
            and 'signVector2' in request.POST \
            and 'signVector3' in request.POST:
        user_id = request.POST['userId']
        signs = [request.POST['signVector1'], request.POST['signVector2'], request.POST['signVector3']]

        result, status = SignValidator.is_sign_valid(signs, sign_len=4)
        if result is True:
            proceed_user_id, proceed_signs = Sign.cast_data_to_numeric_val(user_id=user_id, signs=signs)
            status, msg = SignDB.add_user(proceed_user_id, proceed_signs)

    return render(
        request,
        'create_account.html',
        {
            'form': create_account_form,
            'status': msg
        }
    )
