# Generated by Django 3.1.1 on 2020-09-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement_app', '0003_auto_20200920_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='procurementoffermodel',
            name='company_a_proc_id',
            field=models.CharField(default='PROC-001', max_length=100),
            preserve_default=False,
        ),
    ]