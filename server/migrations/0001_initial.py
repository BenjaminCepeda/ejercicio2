# Generated by Django 3.2.7 on 2021-09-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queryDate', models.DateTimeField(auto_now=True, verbose_name='QueryDate')),
                ('temperature', models.FloatField(verbose_name='Temperature')),
                ('humidity', models.IntegerField(verbose_name='Humidity')),
            ],
        ),
    ]
