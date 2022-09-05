# Generated by Django 4.1 on 2022-08-23 10:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0004_alter_client_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='mobile_operator_code',
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be in the format: 7XXXXXXXXXX', regex='^7\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='message',
            name='client_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailing_service.client'),
        ),
    ]