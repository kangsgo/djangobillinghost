# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0002_auto_20160608_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caritem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('sum_price', models.FloatField(default=0, verbose_name=b'\xe5\xb0\x8f\xe8\xae\xa1')),
                ('products', models.ForeignKey(verbose_name=b'\xe8\xb4\xad\xe7\x89\xa9\xe8\xbd\xa6\xe6\x9d\xa1\xe7\x9b\xae', to='hosts.HostProducts')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u8f66\u6761\u76ee',
                'verbose_name_plural': '\u8d2d\u7269\u8f66\u6761\u76ee',
            },
        ),
    ]
