#coding:utf8

from django.contrib import admin
from banner.models import Banner
from banner.forms import BannerAdminForm
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
	list_display = ('image_tag', 'link','weight','format_date')
	readonly_fields = ('image_tag',)
	fields = ('image','image_tag','link','weight','text')

	form = BannerAdminForm

	def format_date(self,obj):
		return obj.pub_date.strftime("%Y-%m-%d %H:%M:%S")

	format_date.short_description = u"发布时间"
	format_date.admin_order_field = 'pub_date'

admin.site.register(Banner, BannerAdmin)

