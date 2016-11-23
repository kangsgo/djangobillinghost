# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0006_auto_20160610_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostzone',
            name='zoneaccount',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x90\x8d', blank=True),
        ),
        migrations.AlterField(
            model_name='hostzone',
            name='zonepassword',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\xaf\x86\xe7\xa0\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='hostzone',
            name='zoneurl',
            field=models.URLField(max_length=100, null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
    ]
