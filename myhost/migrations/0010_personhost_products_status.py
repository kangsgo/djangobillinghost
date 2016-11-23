# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0009_auto_20160609_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='personhost',
            name='products_status',
            field=models.CharField(default=b'P', max_length=2, choices=[(b'Y', b'active'), (b'P', b'Pengding'), (b'N', b'Delete')]),
        ),
    ]
