# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Develop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430')),
                ('oblast', models.CharField(max_length=256, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c')),
                ('sreda', models.CharField(max_length=256, verbose_name='\u0421\u0440\u0435\u0434\u0430')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438',
                'verbose_name_plural': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('content', tinymce.models.HTMLField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.ImageField(upload_to=b'media', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435-', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='title',
            name='img',
            field=models.ImageField(upload_to=b'media', blank=True),
            preserve_default=True,
        ),
    ]
