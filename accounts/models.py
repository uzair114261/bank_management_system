from django.db import models
from banks.models import  Bank
from authentication.models import User

class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank_account')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_account')
    balance = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.bank} for {self.user}'