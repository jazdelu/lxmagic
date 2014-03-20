#coding:utf8
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
import datetime
from django.utils.timezone import utc
# Create your models here.
class Category(MPTTModel):
	name = models.CharField(max_length = 128, verbose_name = u'分类名称')
	slug = models.SlugField(max_length = 128,help_text=u'只能使用字母和数字且各级分类slug唯一',unique = True)
	parent = TreeForeignKey('self',verbose_name = u'上级分类',null = True, blank = True,related_name = 'children')
	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name = u'产品分类'
		verbose_name_plural = u'产品分类'

	def __unicode__(self):
		return self.name

	def get_url(self):
		url = '/product/'	
		url_temp = ''
		c = self
		while c.get_level()>=0:
			url_temp = c.slug +'/'+ url_temp
			c = c.parent
			if not c:
				break;
		url = url+url_temp
		return url


	def save(self, *args, **kwargs):

		super(Category, self).save(*args, **kwargs)
		Category.objects.rebuild()



class Product(models.Model):
	name = models.CharField(max_length = 128,verbose_name = u'中文名')
	ename = models.CharField(max_length = 128,verbose_name = u'英文名')
	category = TreeForeignKey('Category',related_name = 'products',verbose_name = u'所属分类')
	image = models.ImageField(upload_to='product/', verbose_name = u'图片')
	thumb_small = ImageSpecField(source='image',processors=[ResizeToFit(100)],format='JPEG',options={'quality': 80})
	thumb_middle = ImageSpecField(source='image',processors=[ResizeToFit(150)],format='JPEG',options={'quality': 80})
	thumb_big = ImageSpecField(source='image',processors=[ResizeToFit(400)],format='JPEG',options={'quality': 80})
	spec = models.CharField(max_length = 128,verbose_name = u'规格',blank = True)
	price = models.FloatField(verbose_name = u'价格')
	introduction = models.TextField(verbose_name =u'产品介绍',blank = True)
	instruction = models.TextField(verbose_name = u'使用说明',blank = True)
	pub_date = models.DateTimeField(verbose_name=u'产品发布时间',null = True)
	last_modified = models.DateTimeField(verbose_name=u'最近修改时间', null = True)

	class Meta:
		verbose_name = u'产品'
		verbose_name_plural = u'产品'
		ordering = ['-last_modified',]

	def __unicode__(self):
		return self.name

	def image_tag(self):
		return u'<img src = "%s"/>' % self.thumb_small.url 
	image_tag.short_description = u'预览图'
	image_tag.allow_tags = True

	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.pub_date = datetime.datetime.now()
		self.last_modified = datetime.datetime.now()
		print self.pub_date
		print self.last_modified
		return super(Product, self).save(*args, **kwargs)