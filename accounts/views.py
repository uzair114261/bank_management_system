from django.contrib.admin.templatetags.admin_list import search_form
from django.shortcuts import redirect
from .forms import  AccountForm, SearchForm
from .models import Account
from django.views.generic import  ListView
from banks.models import Bank
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AccountView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Account
    template_name = 'accounts/index.html'
    context_object_name = 'accounts'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        form = AccountForm()
        search_form = SearchForm()
        account = ""
        if request.method == "GET":
            search_username = request.GET.get("username", '')
            if search_username:
                account = Account.objects.filter(username=search_username).select_related('bank','username')
            else:
                account = Account.objects.all().select_related('bank','username')
        context = self.get_context_data()
        context['accounts'] = account
        context['form'] = form
        context['search_form'] = search_form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)