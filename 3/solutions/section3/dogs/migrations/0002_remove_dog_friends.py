# Generated by Django 3.0.6 on 2020-07-02 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='friends',
        ),
    ]