# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('group_yum', '0003_auto_20141005_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime.now(), verbose_name=b'Date Joined'),
            preserve_default=False,
        ),
    ]
