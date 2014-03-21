#coding:utf8
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from product.models import Category
# Create your models here.
LOCATION_CHOICES = (
	('header','header'),
	('sidebar','sidebar'),
	('footer','footer'),
)

MENUITEM_CATEGORY_CHOICES = (
	('category',u'产品分类'),
	('news',u'产品活动页面'),
	('link',u'自定义页面'),
)



class Menu(models.Model):
	name = models.CharField(max_length = 128,verbose_name = u'菜单栏名称')
	location = models.CharField(max_length = 128,choices = LOCATION_CHOICES,verbose_name = '菜单位置')
	markup = models.CharField(max_length = 128,blank = True, null = True)
	is_active = models.BooleanField(verbose_name = '是否使用该菜单')

	class Meta:
		verbose_name = u'菜单栏'
		verbose_name_plural = u'菜单栏'

	def __unicode__(self):
		return self.name
	

class MenuItem(MPTTModel):
	menu = models.ForeignKey(Menu,verbose_name = u'所属菜单栏',related_name = 'menuitems')
	parent = TreeForeignKey('self',verbose_name = u'所属菜单项',null = True, blank = True,related_name = 'children',help_text = u'不选则为一级菜单')
	name = models.CharField(max_length = 128,verbose_name =u'菜单项目名称')
	link_type = models.CharField(max_length = 128,verbose_name = u'菜单类型',choices = MENUITEM_CATEGORY_CHOICES)
	category = TreeForeignKey('product.Category',verbose_name = u'产品分类目录', blank = True, null = True,related_name = 'menuitems')
	link = models.URLField(verbose_name = '链接地址',help_text = u'例: http://www.hklxmagic.com/product/  所有商品列表')
	order = models.IntegerField(verbose_name = u'菜单项顺序',help_text = u'必须为整数,菜单顺序将按从大到小排列')

	class MPTTMeta:
		order_insertion_by = ['menu','-order']

	class Meta:
		verbose_name = u'菜单项'
		verbose_name_plural = u'菜单项'

	def __unicode__(self):
		return self.name