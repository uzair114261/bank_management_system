from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    birthday = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)