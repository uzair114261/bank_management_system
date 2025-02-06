from django.db import models

# Create your models here.
class Accounts(models.Model):
    account_bank = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    account_balance = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.account_bank} for {self.username}'