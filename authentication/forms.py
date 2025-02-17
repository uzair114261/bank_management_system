from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
