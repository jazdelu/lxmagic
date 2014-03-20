#coding:utf8
from banner.models import Banner
from django.forms import ModelForm, ValidationError
from django.core.files.images import get_image_dimensions
from suit.widgets import AutosizedTextarea,NumberInput
class BannerAdminForm(ModelForm):
	class Meta:
		model = Banner
		widgets = {
			'text':AutosizedTextarea(attrs={'row':3,'class':'input-xlarge'}),
			'weight': NumberInput(attrs={'class': 'input-mini'})
		}
	def clean_image(self):
		image = self.cleaned_data.get("image")
		if not image:
			raise ValidationError(u"请选择一张图片!")
		else:
			w, h = get_image_dimensions(image)
			if w < 1440:
				raise ValidationError(u"幻灯片的图片宽度不能低于1440px!")

		return image

	def clean(self):
		if Banner.objects.all().count() == 5:
			raise ValidationError(u'幻灯片已达数量上限!')
		else:
			pass

		return super(BannerAdminForm,self).clean()


		