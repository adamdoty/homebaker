# Generated by Django 4.1.1 on 2022-09-21 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treat',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
