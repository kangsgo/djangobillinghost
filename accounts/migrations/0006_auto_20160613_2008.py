# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_deposit_counmoney'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deposit',
            options={'ordering': ['id'], 'verbose_name': '\u4ee3\u91d1\u5377', 'verbose_name_plural': '\u4ee3\u91d1\u5377'},
        ),
    ]
