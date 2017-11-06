"""
Blog Controller
Author: Ayo Ayco

Takes in requests and returns responses accordingly.

"""

import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def index(request):
    """ index(request) -> response """
    print(request)
    return HttpResponse("Hello World!")

def today_is(request):
    """ displays current date and time """
    return render(request, 'blog/datetime.html', {'now': datetime.datetime.now(), 'base_dir': settings.BASE_DIR})
        