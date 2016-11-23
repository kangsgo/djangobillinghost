# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=12, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x98\xb5\xe7\xa7\xb0', blank=True)),
                ('use_gravatar', models.BooleanField(default=True)),
                ('avatar_url', models.URLField(null=True, blank=True)),
                ('usermoney', models.IntegerField(default=0, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe4\xbd\x99\xe9\xa2\x9d')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
