from django.db import models
from django.contrib.auth.models import AbstractUser

# All the user accounts inherit from UserAccount model


class UserAccount(AbstractUser):
    ACCOUNT_TYPES = [
        ('Manager', 'Manager'),
        ('Landlord', 'Landlord'),
        ('Tenant', 'Tenant'),
    ]
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    # remove username as default for auth
    username = None
    # set email as unique identifier for auth
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        abstract = True

# Tenants Model


class Tenant(UserAccount):
    budget = models.PositiveIntegerField()
    prefered_location = models.CharField(max_length=250)
    dp = models.ImageField(upload_to='Images/Dp/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Landlords Model


class Landlord(UserAccount):
    dp = models.ImageField(upload_to='Images/Dp/')
    company_name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Managers Model


class PropertyManager(UserAccount):
    license_number = models.CharField(max_length=200)
    experience = models.IntegerField()
    services = models.CharField(max_length=255)
    dp = models.ImageField(upload_to='Images/Dp/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
