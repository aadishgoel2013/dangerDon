# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 02:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='alnum_logo',
            new_name='album_logo',
        ),
    ]
