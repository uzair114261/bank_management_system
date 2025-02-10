from django.shortcuts import redirect
from .forms import  AccountForm
from .models import Account
from django.views.generic import  ListView
from banks.models import Bank
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.
class AccountView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Account
    template_name = 'accounts/index.html'
    context_object_name = 'accounts'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        form = AccountForm()
        account = ""
        if request.method == "GET":
            search_name = request.GET.get("search_name", '')
            if search_name:
                account = Account.objects.filter(
                    Q(user__first_name=search_name) | Q(user__last_name=search_name)
                ).select_related('bank','user')
            else:
                account = Account.objects.all().select_related('bank','user')
        context = self.get_context_data()
        context['accounts'] = account
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