# Generated by Django 2.2.9 on 2020-02-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0005_auto_20200204_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
