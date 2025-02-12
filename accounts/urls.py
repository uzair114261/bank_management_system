from django.urls import  path
from . import  views
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('', never_cache(views.AccountView.as_view()), name='account_list'),
]
