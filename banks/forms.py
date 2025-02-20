from  django import  forms
from .models import Bank

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['bank_name', 'branch_name', 'is_islamic']
        widgets = {
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_islamic': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }