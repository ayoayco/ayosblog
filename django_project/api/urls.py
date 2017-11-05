"""
API Endpoints
Author: Ayo Ayco

The urlpatterns must be updated for each API Endpoint
"""

from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.index, name='api_index'),
]
