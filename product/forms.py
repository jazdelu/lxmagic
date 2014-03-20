#coding:utf8

from product.models import Product
from django.forms import ModelForm, ValidationError
from suit.widgets import AutosizedTextarea,EnclosedInput
from mptt.forms import TreeNodeChoiceField

class ProductAdminForm(ModelForm):


	class Meta:
		model = Product
		widgets = {
			'introduction':AutosizedTextarea(attrs={'row':5,'class':'input-xlarge'}),
			'instruction':AutosizedTextarea(attrs={'row':5,'class':'input-xlarge'}),
			'price': EnclosedInput(prepend=u'¥',attrs={'class':'input-mini'}),
		}
	


