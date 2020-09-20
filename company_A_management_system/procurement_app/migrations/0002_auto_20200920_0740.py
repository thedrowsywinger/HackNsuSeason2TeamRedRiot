# Generated by Django 3.1.1 on 2020-09-20 07:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('procurement_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='procurementoffermodel',
            name='issue_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procurementoffermodel',
            name='vendor_unique_code',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
