"""
API Controller
Author: AyoAyco

"""

from django.http import HttpResponse

def index(request):
    """ Index view
        This is just a page to show the API is up.
    """
    return HttpResponse('This is the Blog API. It is working! For API endpoints see documentation.')

# API Endpoints
