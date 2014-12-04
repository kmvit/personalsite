# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headermenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('url', models.CharField(unique=True, max_length=256, verbose_name='\u041f\u0443\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u041f\u0443\u043d\u043a\u0442',
                'verbose_name_plural': '\u041c\u0435\u043d\u044e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(verbose_name='\u041f\u0443\u0442\u044c')),
                ('firstline', tinymce.models.HTMLField(verbose_name='\u041f\u0435\u0440\u0432\u044b\u0439 \u0431\u043b\u043e\u043a', blank=True)),
                ('secondline', tinymce.models.HTMLField(verbose_name='\u0412\u0442\u043e\u0440\u043e\u0439 \u0431\u043b\u043e\u043a')),
            ],
            options={
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('img', models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435-', blank=True)),
                ('content', tinymce.models.HTMLField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('client', models.CharField(max_length=256, verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('service', models.CharField(max_length=256, verbose_name='\u0427\u0442\u043e \u0434\u0435\u043b\u0430\u043b')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, blank=True)),
                ('img', models.ImageField(upload_to=b'', blank=True)),
                ('titlebig', models.CharField(max_length=512, blank=True)),
                ('titlelitle', models.CharField(max_length=512, blank=True)),
            ],
            options={
                'verbose_name': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0430\u0439\u0442\u0430',
                'verbose_name_plural': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u0441\u0430\u0439\u0442\u0430',
            },
            bases=(models.Model,),
        ),
    ]
