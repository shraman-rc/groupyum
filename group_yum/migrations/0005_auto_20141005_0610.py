# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('group_yum', '0004_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='living_group',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(verbose_name=datetime.datetime(2014, 10, 5, 6, 10, 24, 51000)),
        ),
    ]
