# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0006_portfolio_ident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='img',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='img1',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name='\u041c\u0438\u043d\u0438\u0430\u0442\u044e\u0440\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='img2',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='ident',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
