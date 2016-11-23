# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0014_auto_20160609_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personhost',
            name='domain',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9f\x9f\xe5\x90\x8d', blank=True),
        ),
    ]
