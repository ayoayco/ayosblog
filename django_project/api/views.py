"""
API Controller
Author: AyoAyco

"""

from django.http import HttpResponse

def index(request):
    """ Index view
        This is just a page to show the API is up.
    """
    res = """
    <html>
        <h1>This is the Blog API</h1>
        <h3>For API Endpoints, see documentation.</h3>
    </html>
    """

    return HttpResponse(res)

# API Endpoints
