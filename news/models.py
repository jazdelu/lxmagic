#coding:utf8
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from redactor.fields import RedactorField
import datetime

# Create your models here.
class News(models.Model):
	name = models.CharField(max_length = 128,verbose_name=u'活动名称')
	cover = models.ImageField(upload_to= 'news/',verbose_name = u'活动封面')
	thumb_small= ImageSpecField(source=u"cover",processors=[ResizeToFit(100)],format="JPEG",options={"quality": 80})	
	thumb_middle= ImageSpecField(source=u"cover",processors=[ResizeToFill(350,230)],format="JPEG",options={"quality": 80})	
	content = models.TextField(verbose_name = u'活动内容')
	pub_date = models.DateTimeField(verbose_name = u'发布时间',blank = True, null = True,default = datetime.datetime.now())
	last_modified = models.DateTimeField(verbose_name = u'最近修改时间',blank = True, null = True,default = datetime.datetime.now())

	class Meta:
		verbose_name = u'产品活动'
		verbose_name_plural = u'产品活动'
		ordering = ['-pub_date',]

	def __unicode__(self):
		return self.name

	def image_tag(self):
		return u'<img src = "%s"/>' % self.thumb_small.url 
	image_tag.short_description = u'预览图'
	image_tag.allow_tags = True

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if self.id:
			self.last_modified = datetime.datetime.now()
		else:
			pass
		return super(News, self).save(*args, **kwargs)

