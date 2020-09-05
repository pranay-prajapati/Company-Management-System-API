from django.db import models
from django.core.validators import RegexValidator


class Employee(models.Model):
    class Dept(models.IntegerChoices):
        it = 1, "IT"
        hr = 2, "HR"
        cd = 3, "Creative Design"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    dob = models.DateField(max_length=30, blank=True, null=True, default=None)
    salary = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    dept = models.PositiveSmallIntegerField(max_length=20, choices=Dept.choices, default=Dept.it)
