# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0004_auto_20160608_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostzone',
            name='zoneurl',
            field=models.URLField(max_length=30, null=True, verbose_name=b'\xe7\x99\xbb\xe9\x99\x86', blank=True),
        ),
    ]
