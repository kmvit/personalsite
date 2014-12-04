# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0005_remove_develop_oblast'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='ident',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
