# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0007_auto_20141201_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='img1',
            field=models.ImageField(upload_to=b'media', verbose_name='\u041c\u0438\u043d\u0438\u0430\u0442\u044e\u0440\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img2',
            field=models.ImageField(upload_to=b'media', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
