# Generated by Django 2.2.9 on 2020-02-04 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0004_auto_20200204_0543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pincode',
            new_name='pin_code',
        ),
    ]