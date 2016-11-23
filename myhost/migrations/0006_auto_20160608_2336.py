# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0005_auto_20160608_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personhost',
            name='duration_time',
            field=models.IntegerField(default=3, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
