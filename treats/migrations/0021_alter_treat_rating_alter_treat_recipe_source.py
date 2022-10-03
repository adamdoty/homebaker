# Generated by Django 4.1.1 on 2022-10-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treats', '0020_coupon_redemption_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treat',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')], default='3', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='treat',
            name='recipe_source',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
