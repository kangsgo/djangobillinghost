# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0003_caritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostproducts',
            name='hostpackage',
            field=models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9c\xb0\xe5\x8c\xba', to='hosts.HostZone'),
        ),
    ]
