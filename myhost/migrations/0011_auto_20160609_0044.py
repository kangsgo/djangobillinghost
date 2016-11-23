# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0010_personhost_products_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='personhost',
            name='paccounts',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe8\xb4\xa6\xe6\x88\xb7\xe5\x90\x8d', blank=True),
        ),
        migrations.AddField(
            model_name='personhost',
            name='ppassword',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xaf\x86\xe7\xa0\x81', blank=True),
        ),
    ]
