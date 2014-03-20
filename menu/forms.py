#coding:utf8
from django import forms
from django.forms import ModelForm
from menu.models import Menu, MenuItem
from product.models import Category
from mptt.forms import TreeNodeChoiceField

MENUITEM_CATEGORY_CHOICES = (
	('category',u'产品分类'),
	('link',u'自定义页面'),
)

class MenuItemAdminForm(ModelForm):

	class Meta:
		model = MenuItem

	class Media:
		js = ('/static/lxmagic/js/admin_extra.js',)

