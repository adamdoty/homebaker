# Generated by Django 4.1.1 on 2022-10-05 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treats', '0024_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='recipient',
        ),
        migrations.AlterField(
            model_name='event',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='treats.coupon'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
