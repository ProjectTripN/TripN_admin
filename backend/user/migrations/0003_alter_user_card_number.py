# Generated by Django 3.2.5 on 2021-12-27 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_reg_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card_number',
            field=models.BigIntegerField(verbose_name=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
