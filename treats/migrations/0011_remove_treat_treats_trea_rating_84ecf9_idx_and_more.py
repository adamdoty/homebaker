# Generated by Django 4.1.1 on 2022-09-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treats', '0010_alter_treat_slug'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='treat',
            name='treats_trea_rating_84ecf9_idx',
        ),
        migrations.AddIndex(
            model_name='treat',
            index=models.Index(fields=['-rating'], name='treats_trea_rating_8e628d_idx'),
        ),
    ]
