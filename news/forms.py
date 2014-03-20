#coding:utf8

from news.models import News
from django.forms import ModelForm, ValidationError
from suit.widgets import SuitSplitDateTimeWidget
from redactor.widgets import RedactorEditor

class NewsAdminForm(ModelForm):
	class Meta:
		news = News
		widgets = {
			'pub_date': SuitSplitDateTimeWidget,
			'last_modified': SuitSplitDateTimeWidget,
			'content': RedactorEditor(
				redactor_options={'lang': 'en', 'focus': 'true'},
				upload_to='tmp/',
				allow_file_upload=True,
				allow_image_upload=True),
		}