# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0007_auto_20160610_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostproducts',
            name='hostproperty',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\xa5\x97\xe9\xa4\x90\xe5\xb1\x9e\xe6\x80\xa7', blank=True),
        ),
    ]
