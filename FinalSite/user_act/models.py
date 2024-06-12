from django.db import models

# Create your models here.

class Account(models.Model):
    user_name = models.CharField(max_length=16)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=32)

    def __str__(self):
        return f'Username: {self.user_name}, email: {self.email}'
