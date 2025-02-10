from django.db import models
from banks.models import  Bank
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_holder')
    balance = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.bank} for {self.user}'