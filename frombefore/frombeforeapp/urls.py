from django.urls import path
from . import views

""" path(패턴, view, 키워드 인수, name) """
urlpatterns = [
    # ex: /frombefore/
    path('', views.message, name='index'),
    # ex: /frombefore/test
    path('test', views.test, name='test'),
]