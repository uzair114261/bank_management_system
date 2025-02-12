from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from .forms import UserForm
from django.views.generic.edit import CreateView
from django.urls import  reverse_lazy
from django.views import View
from django.contrib.auth import logout

# Create your views here.
class Register(CreateView):
    template_name = 'auth/register.html'
    success_url = reverse_lazy('account_list')
    form_class = UserForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Hash the password
        user.save()
        redirect('login')
        return super().form_valid(form)

class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('account_list')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')