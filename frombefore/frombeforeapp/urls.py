from django.urls import path
from . import views

""" path(패턴, view, 키워드 인수, name) """
urlpatterns = [
    # ex: /frombefore/
    path('', views.IndexView.as_view(), name='index'),
]