from django.db import models
from banks.models import  Bank
from authentication.models import User

# Create your models here.
class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account')
    balance = models.PositiveIntegerField()

    class Meta:
        unique_together = ('user', 'bank')
    def __str__(self):
        return f'{self.bank} for {self.user}'