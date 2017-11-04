"""
Blog Controller
Author: Ayo Ayco
"""

import datetime
from django.http import HttpResponse

def index(request):
    """ index(request) -> response """
    return HttpResponse("Hello World!")

def today_is(request):
    """ displays current date and time """
    now = datetime.datetime.now()
    res = """<html>
                <body>
                    <h1>Today is {0}</h1>
                </body>
            </html>""".format(now)
    return HttpResponse(res)
