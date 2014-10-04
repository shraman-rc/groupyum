# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group_yum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='users',
            new_name='user',
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='groupname', max_length=200),
            preserve_default=False,
        ),
    ]
