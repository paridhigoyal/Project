# Generated by Django 2.2.9 on 2020-02-19 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0014_auto_20200219_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_request', models.TextField(default='')),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportation.Deal')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportation.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='QueryResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_response', models.TextField(default='')),
                ('request_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transportation.QueryRequest')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportation.Profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Query',
        ),
    ]
