# Generated by Django 4.2.7 on 2023-11-03 20:56

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
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdrawal_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account_holder_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
