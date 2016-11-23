# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zonename', models.CharField(max_length=30, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9c\xb0\xe5\x8c\xba')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5730\u533a',
                'verbose_name_plural': '\u5730\u533a',
            },
        ),
        migrations.AddField(
            model_name='hostproducts',
            name='hostsize',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\xa9\xba\xe9\x97\xb4\xe5\xa4\xa7\xe5\xb0\x8f'),
        ),
        migrations.AddField(
            model_name='hostproducts',
            name='hosttraffic',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9c\x88\xe6\xb5\x81\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='hostproducts',
            name='hostpackage',
            field=models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xa5\x97\xe9\xa4\x90', to='hosts.HostZone'),
        ),
        migrations.DeleteModel(
            name='HostPackage',
        ),
    ]
