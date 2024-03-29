# Generated by Django 3.0.3 on 2020-09-04 10:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0003_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='contact',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
