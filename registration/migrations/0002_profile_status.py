# Generated by Django 4.2.7 on 2023-11-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
