from django.db import models
from banks.models import  Bank
from authentication.models import User

class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='accounts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    balance = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.bank} for {self.user}'