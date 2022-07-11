# Generated by Django 4.0.5 on 2022-06-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Token')),
                ('tg_chat_id', models.CharField(max_length=200, verbose_name='Chat ID')),
                ('tg_message', models.TextField(verbose_name='Message Text')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
    ]