from django.contrib import admin
from .models import  Accounts

# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ['account_bank', 'username', 'account_balance']

admin.site.register(Accounts, BankAdmin)