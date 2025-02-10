from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import BankForm
from .models import Bank
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class BankView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Bank
    template_name = 'banks/index.html'
    context_object_name = 'banks'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        form = BankForm()
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('banks_list')
        # self.object_list = self.get_queryset()
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)