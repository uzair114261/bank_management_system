from django.urls import  path
from . import  views

urlpatterns = [
    path('', views.BankView.as_view(), name='banks_list'),
]
