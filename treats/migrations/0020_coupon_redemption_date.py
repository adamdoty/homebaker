# Generated by Django 4.1.1 on 2022-10-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treats', '0019_alter_profile_is_baker_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='redemption_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
