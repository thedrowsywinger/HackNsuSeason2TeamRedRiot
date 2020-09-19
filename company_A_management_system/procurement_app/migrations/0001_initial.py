# Generated by Django 3.1.1 on 2020-09-19 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcurementOfferModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_quantity', models.FloatField()),
                ('product_price_per_unit', models.FloatField()),
                ('status', models.FloatField()),
            ],
        ),
    ]
