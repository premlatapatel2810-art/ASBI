from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Account(models.Model):
    Username = models.CharField(max_length=100,unique=True,null=False)
    Password = models.CharField(unique=True,null=False,max_length=50)
    Account_Number = models.CharField(
        max_length=6,
        validators=[MinLengthValidator(6)],
        unique=True,
        null=False
        )
    Balance = models.DecimalField(decimal_places=2,null=False,unique=False,max_digits=10)


    Account_choises = [
        ('S', 'Savings'),
        ('C', 'Current')
    ]
    Account_type = models.CharField(max_length=1,choices=Account_choises,default='S')

    def __str__(self):
        return self.Username
    
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('D', 'Deposit'),
        ('W', 'Withdrawal')
    ]
    Transaction_type = models.CharField(choices=TRANSACTION_TYPES,max_length=1)
    Time = models.DateTimeField(auto_now_add=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Account_Number = models.CharField(
        max_length=6,
        validators=[MinLengthValidator(6)],
        unique=True,
        null=False
        )