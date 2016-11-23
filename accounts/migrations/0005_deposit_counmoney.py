# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='counmoney',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x87\x91\xe9\xa2\x9d'),
        ),
    ]
