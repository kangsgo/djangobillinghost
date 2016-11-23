# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0015_auto_20160611_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sitedomain', models.CharField(default=b'http://billvm.com', max_length=50, verbose_name=b'zhandianyuming')),
            ],
        ),
        migrations.AddField(
            model_name='personblling',
            name='trade_no',
            field=models.CharField(default=0, max_length=50, verbose_name=b'jiaoyihao'),
        ),
    ]
