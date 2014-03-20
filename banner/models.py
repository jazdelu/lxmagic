#coding:utf8

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
import datetime
# Create your models here.
class Banner(models.Model):
	image = models.ImageField(upload_to=u'banner/',verbose_name=u"选择图片",help_text = u'请选择宽度不小于1440px的图片')
	thumb= ImageSpecField(source=u"image",processors=[ResizeToFit(100)],format="JPEG",options={"quality": 80})	
	link = models.URLField(verbose_name=u"幻灯片链接",help_text=u'例:http://www.example.com/example/')
	text = models.TextField(verbose_name = '相关描述',blank = True)
	weight = models. IntegerField(verbose_name = u'权重',default = 1)
	pub_date = models.DateTimeField(verbose_name = u'幻灯片发布时间',null = True, blank = True)
	last_modified = models.DateTimeField(verbose_name = u'最近修改时间',null = True, blank = True)

	class Meta:
		verbose_name = u'首页幻灯片'
		verbose_name_plural = u'首页幻灯片'
		ordering = ['-weight','-pub_date',]

	def __unicode__(self):
		return self.image.url

	def image_tag(self):
		return u'<img src = "%s"/>' % self.thumb.url 
	image_tag.short_description = u'预览图'
	image_tag.allow_tags = True

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.pub_date = datetime.datetime.now()
		self.last_modified = datetime.datetime.now()
		return super(Banner, self).save(*args, **kwargs)