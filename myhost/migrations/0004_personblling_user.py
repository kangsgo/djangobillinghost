# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhost', '0003_auto_20160608_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='personblling',
            name='user',
            field=models.ForeignKey(related_name='myblling', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
