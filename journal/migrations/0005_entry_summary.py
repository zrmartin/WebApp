# Generated by Django 2.0.1 on 2018-01-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0004_auto_20180128_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='summary',
            field=models.TextField(default='You have not written a summary for today yet.'),
        ),
    ]
