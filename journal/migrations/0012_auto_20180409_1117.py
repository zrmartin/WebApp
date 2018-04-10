# Generated by Django 2.0.1 on 2018-04-09 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0011_auto_20180317_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='concert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concert', to='journal.Concert'),
        ),
    ]
