# Generated by Django 5.0 on 2024-08-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_mailing_send_name_alter_message_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='frequency',
            field=models.CharField(blank=True, choices=[('once', 'Разово'), ('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], max_length=20, null=True, verbose_name='периодичность'),
        ),
    ]
