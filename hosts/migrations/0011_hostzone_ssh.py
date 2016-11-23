# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0010_auto_20160611_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostzone',
            name='ssh',
            field=models.CharField(default=b'2083', max_length=5, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xab\xaf\xe5\x8f\xa3'),
        ),
    ]
