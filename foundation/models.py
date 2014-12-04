from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone 

      

class Title(models.Model):
    name = models.CharField(max_length=512, blank=True)
    img = models.ImageField(upload_to='media', blank=True)
    img2 = models.ImageField(upload_to='media',null=True, blank=True)
    titlebig = models.CharField(max_length=512, blank=True)
    titlelitle = models.CharField(max_length=512, blank=True)
    class Meta:
        verbose_name = u'Заголовок сайта'
        verbose_name_plural = u'Заголовки сайта'
        
    def __unicode__(self):
        return self.name
    
class Page(models.Model):
    title = models.CharField(max_length=256, verbose_name=u"Название")
    slug = models.SlugField(verbose_name=u"Путь")
    firstline = HTMLField(blank=True,verbose_name=u"Первый блок")
    secondline = HTMLField(verbose_name=u"Второй блок")


    class Meta:   verbose_name_plural = u'Страницы'

    def __unicode__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=256, verbose_name=u"Название")
    ident = models.IntegerField(blank=True)
    img1 = models.ImageField(upload_to='media', verbose_name=u"Миниатюра")
    img2 = models.ImageField(upload_to='media', verbose_name=u"Изображение")
    content = HTMLField(blank=True,verbose_name=u"Описание")
    client = models.CharField(max_length=256, verbose_name=u"Клиент")
    data = models.DateTimeField(default=timezone.now)
    service = models.CharField(max_length=256, verbose_name=u"Что делал")
    class Meta:
        verbose_name = u'Изображение'
        verbose_name_plural = u'Портфолио'
        
    def __unicode__(self):
        return self.title

class Develop(models.Model):
    title = models.CharField(max_length=256, verbose_name=u"Разработка")
    sreda = models.CharField(max_length=256, verbose_name=u"Среда")

    class Meta:
        verbose_name = u'Разработку'
        verbose_name_plural = u'Разработки'

    def __unicode__(self):
        return self.title


class Information(models.Model):
    title = models.CharField(max_length=256, verbose_name=u"Название")
    content = models.TextField(blank=True,verbose_name=u"Описание")

    class Meta:
        verbose_name = u'Контактная информацию'
        verbose_name_plural = u'Контактная информация'

    def __unicode__(self):
        return self.title
    
class Headermenu(models.Model):
    name = models.CharField(max_length=256, unique=True,  verbose_name=u"Название")
    url = models.CharField(max_length=256, unique=True,  verbose_name=u"Путь")
    class Meta:
        verbose_name = u'Пункт'
        verbose_name_plural = u'Меню'


    def __unicode__(self):
        return self.name
