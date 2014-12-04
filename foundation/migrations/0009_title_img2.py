# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0008_auto_20141201_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='img2',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
            preserve_default=True,
        ),
    ]
