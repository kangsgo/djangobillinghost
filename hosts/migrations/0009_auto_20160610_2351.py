# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0008_hostproducts_hostproperty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostzone',
            name='zonepassword',
            field=models.TextField(null=True, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\xaf\x86\xe9\x92\xa5', blank=True),
        ),
    ]
