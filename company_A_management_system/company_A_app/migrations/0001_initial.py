# Generated by Django 3.1.1 on 2020-09-20 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company_email', models.CharField(max_length=250)),
                ('company_role', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAInventoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_quantity', models.FloatField()),
                ('product_unit', models.CharField(max_length=50)),
                ('product_price_per_unit', models.FloatField()),
                ('company_a_product_id', models.IntegerField()),
                ('product_added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_A_app.profilemodel')),
            ],
        ),
    ]
