from django import  forms
from .models import  Accounts

class AccountForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ['account_bank', 'username', 'account_balance']
        widgets = {
            'account_bank': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'account_balance': forms.TextInput(attrs={'class': 'form-control'}),
        }