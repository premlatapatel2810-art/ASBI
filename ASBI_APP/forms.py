from django import forms

class Account_Creation(forms.Form):
    Username = forms.CharField(max_length=100, required=True)
    Password = forms.CharField(widget=forms.PasswordInput, required=True,max_length=50)
    Account_Number = forms.IntegerField(
        max_length=6,
        min_length=6,
        required=True
    )
    Account_choises = [
        ('S', 'Savings'),
        ('C', 'Current')
    ]
    Account_type = forms.ChoiceField(choices=Account_choises)

class Transaction(forms.Form):
    TRANSACTION_TYPES = [
        ('D', 'Deposit'),
        ('W', 'Withdrawal')
    ]
    Transaction_type = forms.CharField(choices=TRANSACTION_TYPES,max_length=1)
    Amount = forms.DecimalField(max_digits=10, decimal_places=2)
    Account_Number = forms.CharField(
        max_length=6,
        min_length=6,
        required=True
    )