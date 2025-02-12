from django.urls import path
from . import  views

urlpatterns = [
    path('api/list_all_banks', views.Banks.as_view()),
    path('api/add_new_bank', views.BankCreateView.as_view())
]
