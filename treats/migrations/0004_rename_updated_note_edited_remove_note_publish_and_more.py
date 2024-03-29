# Generated by Django 4.1.1 on 2022-09-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treats', '0003_alter_treat_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='updated',
            new_name='edited',
        ),
        migrations.RemoveField(
            model_name='note',
            name='publish',
        ),
        migrations.AlterField(
            model_name='treat',
            name='cover_img',
            field=models.ImageField(default='no image', upload_to='images/'),
            preserve_default=False,
        ),
    ]
