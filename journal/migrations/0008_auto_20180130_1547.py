# Generated by Django 2.0.1 on 2018-01-31 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_auto_20180130_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(error_messages={'invalid': 'Invalid date', 'unique_for_date': 'Date must be unique'}, unique_for_date='pub_date', verbose_name='%m/%d/%Y'),
        ),
    ]