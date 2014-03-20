#coding:utf8
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import Menu, MenuItem
from menu.forms import MenuItemAdminForm
from django.contrib.admin import SimpleListFilter
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
	list_display = ('name','location','markup','is_active',)
	fields = ('name','location','markup','is_active',)

class MenuItemAdmin(MPTTModelAdmin):
	mptt_level_indent = 20
	list_filter = ('menu',)
	list_display = ('name','link_type','link','menu','order')
	list_display_links = ('name',)

	form = MenuItemAdminForm

admin.site.register(Menu,MenuAdmin)
admin.site.register(MenuItem,MenuItemAdmin)