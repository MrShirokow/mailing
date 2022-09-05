# Generated by Django 4.1 on 2022-08-23 08:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0002_alter_client_phone_number_alter_message_client_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['id'], 'verbose_name': 'client', 'verbose_name_plural': 'clients'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['id'], 'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['start_datetime'], 'verbose_name': 'notification', 'verbose_name_plural': 'notifications'},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='end_datetime',
            new_name='sending_datetime',
        ),
        migrations.RemoveField(
            model_name='message',
            name='start_datetime',
        ),
        migrations.AddField(
            model_name='message',
            name='is_send',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be in the format: 7XXXXXXXXXX', regex='^7\\d{10}$')]),
        ),
    ]