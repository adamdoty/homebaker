# Manual migration file by Adam in Django 4.1.1 on 2022-09-29 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treats', '0014_coupon_coupon_treats_coup_created_45212d_idx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='reason_for_coupon_date',
            new_name='target_date'
        ),
        migrations.RenameField(
            model_name='coupon',
            old_name='coupon_recipient',
            new_name='recipient'
        ),
        migrations.RenameField(
            model_name='coupon',
            old_name='coupon_reason',
            new_name='reason'
        ),
    ]
