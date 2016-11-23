# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0006_auto_20160608_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personhost',
            name='duration_time',
            field=models.CharField(default=b'T', max_length=2, choices=[(b'T', b'3'), (b'M', b'30'), (b'Y', b'365'), (b'DY', b'730')]),
        ),
    ]
