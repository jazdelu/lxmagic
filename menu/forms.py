#coding:utf8
from django import forms
from django.forms import ModelForm
from menu.models import Menu, MenuItem
from product.models import Category


class MenuItemAdminForm(ModelForm):

	class Meta:
		model = MenuItem

	class Media:
		js = ('/static/lxmagic/js/admin_extra.js',)

