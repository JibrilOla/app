# Generated by Django 4.2.7 on 2023-11-26 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0006_machinepurchase_recommending_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinepurchase',
            name='recommending_profile',
        ),
        migrations.AlterField(
            model_name='machinepurchase',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 28, 59, 108379, tzinfo=datetime.timezone.utc)),
        ),
    ]