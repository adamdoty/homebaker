# Generated by Django 4.1.1 on 2022-10-06 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treats', '0025_remove_event_recipient_alter_event_coupon_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treat',
            options={'ordering': ['created', 'is_recipient_request']},
        ),
        migrations.RemoveIndex(
            model_name='treat',
            name='treats_trea_rating_84ecf9_idx',
        ),
        migrations.RemoveField(
            model_name='treat',
            name='rating',
        ),
    ]