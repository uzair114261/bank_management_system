from django.urls import  path
from . import  views
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('', never_cache(views.BankView.as_view()), name='banks_list'),
]
