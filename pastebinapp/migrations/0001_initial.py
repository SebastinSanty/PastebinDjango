# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pastebin',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('textpaste', models.CharField(max_length=80)),
                ('pasteurl', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
