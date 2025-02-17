from django.urls import  path
from . import  views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', views.AccountAPIView.as_view(), name='bank_account_apiview'),
    path('generic/bank_account/', views.CreateAccountGenericView.as_view(), name='bank_account_genericview'),
    path('generic/bank_account/<int:user_id>', views.ListAccountGenericAPIView.as_view(), name='bank_account_genericview'),
    path('generic/details/<int:id>', views.AccountActionGenericView.as_view(), name='account_detail_view'),
]
router.register(r'viewset/bank_account', views.BankAccountViewSets, basename='bank_account_viewset')
urlpatterns += router.urls