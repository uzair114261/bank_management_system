from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('signup', views.SignupView.as_view()),
    path('user_operations/<str:username>', views.UserOperations.as_view()),
]