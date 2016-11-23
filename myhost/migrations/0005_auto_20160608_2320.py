# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhost', '0004_personblling_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personblling',
            name='billingdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='personhost',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
