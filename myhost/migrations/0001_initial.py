# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonHost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billingdate', models.DateTimeField(default=datetime.datetime(2016, 6, 8, 14, 58, 58, 476392, tzinfo=utc), verbose_name=b'\xe8\xb4\xa6\xe5\x8d\x95\xe6\x97\xb6\xe9\x97\xb4')),
                ('billingmoney', models.IntegerField(default=0, verbose_name=b'\xe8\xb4\xa6\xe5\x8d\x95\xe9\x87\x91\xe9\xa2\x9d')),
                ('billingstatus', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbb\x98\xe6\xac\xbe')),
            ],
            options={
                'ordering': ['billingdate'],
                'verbose_name': '\u4e2a\u4eba\u8d26\u5355',
                'verbose_name_plural': '\u4e2a\u4eba\u8d26\u5355',
            },
        ),
    ]
