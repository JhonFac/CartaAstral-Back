# Generated by Django 4.0.4 on 2024-04-29 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='carga',
        ),
    ]
