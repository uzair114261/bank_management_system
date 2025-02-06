from django.shortcuts import redirect
from .forms import  AccountForm
from .models import Accounts
from django.views.generic import  ListView

# Create your views here.
class AccountView(ListView):
    model = Accounts
    template_name = 'accounts/index.html'
    context_object_name = 'accounts'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        form = AccountForm()
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)