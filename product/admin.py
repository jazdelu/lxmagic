#coding:utf8
from django.contrib import admin
from product.models import Product, Category
from product.forms import ProductAdminForm
from mptt.admin import MPTTModelAdmin
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	list_display = ('name','ename','image_tag','spec','price','pub_date_format','last_modified_format')
	fieldsets = (
		(u'基本信息', {
			'fields':('name','ename','spec','price','image','image_tag')
		}),
		(u'分类信息',{
			'classes':('suit-3column'),
			'fields':('category',),
		}),
		(u'详细信息',{

			'fields':('introduction','instruction')
		}),
	)
	search_fields = ('name','ename','price',)
	list_filter=('category',)


#	def get_category(self,obj):
#		n = obj.category.name
#		u = '?category__id__exact='+str(obj.category.id)
#		return u'<a href="%s">%s</a>' % (u,n)

#	get_category.short_description = u'所属分类'
#	get_category.allow_tags = True


	def pub_date_format(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")
	pub_date_format.admin_order_field = 'pub_date'
	pub_date_format.short_description = u'产品发布时间'

	def last_modified_format(self,obj):
		return obj.last_modified.strftime("%Y-%m-%d %H:%M:%S")
	last_modified_format.admin_order_field = 'last_modified'
	last_modified_format.short_description = u'最近修改时间'

	form = ProductAdminForm


class CategoryAdmin(MPTTModelAdmin):
	mptt_level_indent = 20
	search_fields = ('name', 'slug')
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'slug', )
	list_display_links = ('name',)




admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)