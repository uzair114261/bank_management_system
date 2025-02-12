from django import  forms
from .models import  Account
from banks.models import Bank
from django.contrib.auth.models import User

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'user', 'balance']

        widgets = {
            'balance': forms.TextInput(attrs={'class': 'form-control'}),
        }
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        to_field_name='username',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    bank = forms.ModelChoiceField(
        queryset=Bank.objects.all(),
        to_field_name='bank_name',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    ),
