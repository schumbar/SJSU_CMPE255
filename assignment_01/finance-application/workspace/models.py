import os  # Import the os module for file size checking
from django.db import models  # Import the models module from Django
from django.contrib.auth.models import User  # Import the User model from Django's authentication system

class Receipt(models.Model):  # Define a Receipt model that inherits from Django's Model class
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Define a foreign key to the User model
    image = models.ImageField(upload_to='receipts/')  # Define an ImageField for the uploaded receipt image
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Define a DateTimeField for the upload time

    def check_file_size(self):  # Define a method to check the size of the uploaded image file
        max_size = 100 * 1024 * 1024  # Define the maximum file size as 100MB in bytes
        return os.path.getsize(self.image.path) < max_size  # Return True if the file size is less than the maximum size, False otherwise

class BankAccount(models.Model):  # Define a BankAccount model that inherits from Django's Model class
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Define a foreign key to the User model
    account_number = models.CharField(max_length=20)  # Define a CharField for the bank account number
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Define a DecimalField for the account balance

class Message(models.Model):  # Define a Message model that inherits from Django's Model class
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Define a foreign key to the User model
    message = models.TextField()  # Define a TextField for the message content
    sent_at = models.DateTimeField(auto_now_add=True)  # Define a DateTimeField for the message send time

class Transaction(models.Model):  # Define a Transaction model that inherits from Django's Model class
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Define a foreign key to the User model
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Define a DecimalField for the transaction amount
    type = models.CharField(max_length=10)  # Define a CharField for the transaction type

class Dispute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=20)
