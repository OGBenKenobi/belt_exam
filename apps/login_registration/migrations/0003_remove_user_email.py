# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-23 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
