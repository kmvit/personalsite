# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0004_auto_20141201_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='develop',
            name='oblast',
        ),
    ]
