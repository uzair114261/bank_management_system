from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_name = models.CharField(max_length=255, unique=True)
    branch = models.CharField(max_length=255)
    is_islamic = models.BooleanField(default=True)

    def __str__(self):
        return self.bank_name