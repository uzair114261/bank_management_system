from django import  forms
from .models import  Account
from banks.models import Bank

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'username', 'balance']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'balance': forms.TextInput(attrs={'class': 'form-control'}),
        }

    bank = forms.ModelChoiceField(
        queryset=Bank.objects.all(),
        to_field_name='bank_name',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    ),