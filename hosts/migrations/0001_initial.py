# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostPackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('packagename', models.CharField(max_length=30, verbose_name=b'\xe5\xa5\x97\xe9\xa4\x90\xe5\x90\x8d\xe7\xa7\xb0')),
                ('packsize', models.IntegerField(default=0, verbose_name=b'\xe7\xa9\xba\xe9\x97\xb4\xe5\xa4\xa7\xe5\xb0\x8f')),
                ('packtraffic', models.IntegerField(default=0, verbose_name=b'\xe6\x9c\x88\xe6\xb5\x81\xe9\x87\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='HostProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=30, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('hostprice', models.FloatField(default=0, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('hostdesc', models.CharField(max_length=100, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\x80\xe4\xbb\x8b')),
                ('hostpackage', models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xa5\x97\xe9\xa4\x90', to='hosts.HostPackage')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1',
            },
        ),
    ]
