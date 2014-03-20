#coding:utf8
from django.contrib import admin
from news.models import News
from news.forms import NewsAdminForm
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	list_display=('name','pub_date_format','last_modified_format')
	fields = ('name','cover','image_tag','content','pub_date')
	readonly_fields = ('image_tag',)
	def pub_date_format(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")
	pub_date_format.admin_order_field = 'pub_date'
	pub_date_format.short_description = u'活动发布时间'

	def last_modified_format(self,obj):
		return obj.last_modified.strftime("%Y-%m-%d %H:%M:%S")
	last_modified_format.admin_order_field = 'last_modified'
	last_modified_format.short_description = u'最近修改时间'

	form = NewsAdminForm

admin.site.register(News,NewsAdmin)
