"""
Definition of views.
"""

from datetime import datetime

from demoapp.knn import check_sign
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
        if check_sign(request.POST['signs']):
            status = 'Пользователь авторизован'
        else:
            status = 'Пользователь не авторизован'
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
