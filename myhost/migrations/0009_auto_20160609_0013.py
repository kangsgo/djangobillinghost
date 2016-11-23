# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0008_auto_20160609_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personhost',
            name='duration_time',
            field=models.CharField(default=b'3', max_length=4, choices=[(b'3', b'3'), (b'30', b'30'), (b'365', b'365'), (b'730', b'730')]),
        ),
    ]
