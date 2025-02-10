from django.db import models
from banks.models import  Bank

# Create your models here.
class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank')
    username = models.CharField(max_length=255)
    balance = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.bank} for {self.username}'