# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0011_hostzone_ssh'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostzone',
            name='servertype',
            field=models.CharField(default=b'cpanel', max_length=2, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'cpanel', b'cpanel')]),
        ),
    ]
