from django.urls import path
from .views import getAPI

urlpatterns = [
    path('api/cryptoprices/', getAPI, name='getAPI'),
]