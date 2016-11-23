# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0013_auto_20160609_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personhost',
            name='duration_time',
            field=models.IntegerField(default=0),
        ),
    ]
