# Generated by Django 2.2.9 on 2020-02-14 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0008_auto_20200210_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='rating',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='transportation.Rating'),
        ),
    ]