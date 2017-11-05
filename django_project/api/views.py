"""
API Controller
Author: AyoAyco

"""

from django.http import HttpResponse

# API Endpoints
def index(request):
    """ Index view
        This is just a page to show the API is up.
    """
    return HttpResponse('This is the Blog API. It is working! For API endpoints see documentation.')
