"""
API Controller
Author: AyoAyco

"""

from django.http import HttpResponse

# Create your views here.
def index(request):
    """ Index view """
    return HttpResponse('This is the Blog API')
