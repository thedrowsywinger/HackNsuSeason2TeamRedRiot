# Generated by Django 3.1.1 on 2020-09-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0004_auto_20200921_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalmodel',
            name='vendor_quantity',
            field=models.FloatField(),
        ),
    ]
