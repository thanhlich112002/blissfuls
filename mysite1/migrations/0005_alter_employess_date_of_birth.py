# Generated by Django 4.1.7 on 2023-04-04 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite1', '0004_employess_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employess',
            name='Date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]