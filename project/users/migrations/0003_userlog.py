# Generated by Django 3.1.6 on 2021-02-16 13:56

import django.contrib.admin.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('users', '0002_auto_20210124_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
            ],
            options={
                'verbose_name': 'Действие',
                'verbose_name_plural': 'История действий',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('admin.logentry',),
            managers=[
                ('objects', django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]
