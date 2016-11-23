# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('counpon', models.CharField(max_length=15, null=True, verbose_name=b'\xe4\xbb\xa3\xe9\x87\x91\xe5\x8d\xb7', blank=True)),
                ('counponactive', models.BooleanField(default=True)),
            ],
        ),
    ]
