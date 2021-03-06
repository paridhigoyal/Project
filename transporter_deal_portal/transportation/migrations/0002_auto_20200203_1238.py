# Generated by Django 2.2.9 on 2020-02-03 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transportation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(default='', max_length=50)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=15)),
                ('man_Year', models.IntegerField()),
                ('Capacity', models.IntegerField()),
                ('picture', models.ImageField(upload_to='')),
                ('document', models.CharField(max_length=100)),
                ('transporter', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='transportation.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('deal_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_Date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.IntegerField()),
                ('rating', models.ManyToManyField(to='transportation.Rating')),
                ('transporter', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='transportation.Profile')),
                ('vehicle_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='transportation.Vehicle')),
            ],
        ),
    ]
