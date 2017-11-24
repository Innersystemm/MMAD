"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def index(request):
    homepageText = 'Welcome to Home Page!\nTime: '

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        {
            'title':'Home Page',
            'date': datetime.now(),
            'text': homepageText,

        }
    )

def articles(request):
    articles = ['srdtfghsdfghjsdfghjkdfghjkfghfhfghfghfhfghfghfghfghfgh',
                'dfgfgdjkfghdfjhgdfhgjdfhgdfjghdfkjghdfjkghdkjfghdfhgjdfhgdfjghdfghdfjghkdfjgjdf',
                'tfjghfjhkgjhkfghlgjhkjghlkghjhkjhghkjhhkfgjhkhjkhjjhfjhfkj']

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'articles.html',
        {
            'articles': articles,
            'title': 'Articles',
            'date': datetime.now(),
        }
    )

def auth(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'auth.html'
    )