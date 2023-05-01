from django.db import models
from django.contrib.auth.models import User

# All the user accounts inherit from UserAccount model
class UserAccount(models.Model):
    ACCOUNT_TYPES = [
        ('Manager', 'Manager'),
        ('Landlord', 'Landlord'),
        ('Tenant', 'Tenant'),
    ]
    account_type = models.CharField(
        max_length=250, choices=ACCOUNT_TYPES, default='Tenant')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=250)

    class Meta:
        abstract = True

# Tenants Model
class Tenant(UserAccount):
    budget = models.PositiveIntegerField()
    prefered_location = models.CharField(max_length=250)
    dp = models.ImageField(upload_to='Images/Dp/')


    def __str__(self):
        return self.first_name

# Landlords Model
class Landlord(UserAccount):
    dp = models.ImageField(upload_to='Images/Dp/')
    company_name = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name

# Managers Model
class PropertyManager(UserAccount):
    license_number = models.CharField(max_length=200)
    experience = models.IntegerField()
    services = models.CharField(max_length=255)
    dp = models.ImageField(upload_to='Images/Dp/')


    def __str__(self):
        return self.first_name
