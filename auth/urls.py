from django.urls import path
from . import views

urlpatterns = [
    path('register_user', views.Register.as_view(), name='register'),
    path('', views.CustomLoginView.as_view(
        template_name='auth/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]