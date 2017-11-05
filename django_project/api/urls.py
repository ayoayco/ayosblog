"""
API Endpoints
Author: Ayo Ayco
"""

from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.index, name='api_index'),
]
