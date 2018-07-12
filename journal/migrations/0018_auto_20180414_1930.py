# Generated by Django 2.0.1 on 2018-04-15 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0017_auto_20180414_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='concert',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
