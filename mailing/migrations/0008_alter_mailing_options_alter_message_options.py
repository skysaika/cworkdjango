# Generated by Django 4.2.9 on 2024-09-17 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_mailing_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'permissions': [('can_view_mailing', 'Can view mailing'), ('can_send_mailing', 'Can send mailing'), ('can_disable_mailing', 'Can disable mailing')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'permissions': [('can_view_message', 'Can view message')], 'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
    ]
