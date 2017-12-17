"""
Definition of views.
"""

from datetime import datetime

from demoapp.knn import check_sign
from demoapp.knn import load_signs
from django.http import HttpRequest
from django.shortcuts import render

from .forms import AuthForm


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
    auth_form = AuthForm()

    if 'signs' in request.POST.keys():
        result = check_sign(request.POST['signs'], request.POST['user_id'])
        if result is True:
            status = 'Пользователь {} авторизован'.format(request.POST['user_id'])
        elif result is False:
            status = 'Пользователь {} не авторизован'.format(request.POST['user_id'])
        else:
            status = 'Пользователь {} не найден'.format(request.POST['user_id'])
    else:
        status = 'Введите данные для авторизации'

    return render(
        request,
        'auth.html',
        {
            'form': auth_form,
            'status': status,
        }
    )


def get_signs(request):
    return load_signs()
