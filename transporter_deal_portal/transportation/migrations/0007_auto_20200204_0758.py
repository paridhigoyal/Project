# Generated by Django 2.2.9 on 2020-02-04 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0006_auto_20200204_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='transporter',
        ),
        migrations.AddField(
            model_name='deal',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transportation.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='transporter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transportation.Profile'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='deal',
            name='rating',
        ),
        migrations.AddField(
            model_name='deal',
            name='rating',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='transportation.Rating'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deal',
            name='vehicle_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transportation.Vehicle'),
        ),
    ]