# Generated by Django 4.2.7 on 2023-11-25 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinepurchase',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 25, 21, 3, 34, 907255, tzinfo=datetime.timezone.utc)),
        ),
    ]
