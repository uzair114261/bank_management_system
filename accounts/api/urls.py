from django.urls import  path
from . import  views

urlpatterns = [
    path('accounts', views.BankAccount.as_view()),
    path('user/<int:bank_id>/<int:user_id>', views.AccountDetailView.as_view()),
]
