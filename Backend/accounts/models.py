from django.db import models
from django.contrib.auth.models import AbstractUser, User

class UserAccount(models.Model):
    ACCOUNT_TYPES = [
        ('Manager', 'Manager'),
        ('Landlord', 'Landlord'),
        ('Tenant', 'Tenant'),
    ]

    account_type = models.CharField(max_length=250, choices=ACCOUNT_TYPES, default=Tenant)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=250)

    class Meta:
        abstract = True
    

class PropertyManager(UserAccount):
    experience = models.IntegerField()
    services = models.CharField(max_length=255)


