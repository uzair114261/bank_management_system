from django.contrib import admin
from .models import  Account

# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ['bank', 'username', 'balance']

admin.site.register(Account, BankAdmin)