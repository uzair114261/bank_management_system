from django.contrib import admin
from .models import  Bank

# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'branch', 'is_islamic']

admin.site.register(Bank, BankAdmin)