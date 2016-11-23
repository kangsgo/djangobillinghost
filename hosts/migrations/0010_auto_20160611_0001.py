# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0009_auto_20160610_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostzone',
            name='zoneurl',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
    ]
