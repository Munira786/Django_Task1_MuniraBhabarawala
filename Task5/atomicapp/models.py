from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - Balance: {self.balance}"
