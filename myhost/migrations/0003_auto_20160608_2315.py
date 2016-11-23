# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0004_auto_20160608_2315'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhost', '0002_auto_20160608_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personblling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billingdate', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe8\xb4\xa6\xe5\x8d\x95\xe6\x97\xb6\xe9\x97\xb4')),
                ('billingmoney', models.IntegerField(default=0, verbose_name=b'\xe8\xb4\xa6\xe5\x8d\x95\xe9\x87\x91\xe9\xa2\x9d')),
                ('billingstatus', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xbb\x98\xe6\xac\xbe')),
            ],
            options={
                'ordering': ['billingdate'],
                'verbose_name': '\u4e2a\u4eba\u8d26\u5355',
                'verbose_name_plural': '\u4e2a\u4eba\u8d26\u5355',
            },
        ),
        migrations.AlterModelOptions(
            name='personhost',
            options={'ordering': ['create_date'], 'verbose_name': '\u4e2a\u4eba\u4e3b\u673a', 'verbose_name_plural': '\u4e2a\u4eba\u4e3b\u673a'},
        ),
        migrations.RemoveField(
            model_name='personhost',
            name='billingdate',
        ),
        migrations.RemoveField(
            model_name='personhost',
            name='billingmoney',
        ),
        migrations.RemoveField(
            model_name='personhost',
            name='billingstatus',
        ),
        migrations.AddField(
            model_name='personhost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 8, 15, 15, 31, 624927, tzinfo=utc), verbose_name=b'\xe5\xbb\xba\xe7\xab\x8b\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personhost',
            name='domain',
            field=models.URLField(max_length=30, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9f\x9f\xe5\x90\x8d', blank=True),
        ),
        migrations.AddField(
            model_name='personhost',
            name='duration_time',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='personhost',
            name='products',
            field=models.ForeignKey(default=1, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\xa5\x97\xe9\xa4\x90', to='hosts.HostProducts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personhost',
            name='user',
            field=models.ForeignKey(related_name='myproduct', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
