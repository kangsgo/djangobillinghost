# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personhost',
            name='billingdate',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe8\xb4\xa6\xe5\x8d\x95\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
