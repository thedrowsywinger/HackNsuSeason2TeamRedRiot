# Generated by Django 3.1.1 on 2020-09-21 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procurement_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acceptedoffermodel',
            name='vendor',
        ),
    ]
