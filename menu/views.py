from django.shortcuts import render
from django.http import HttpResponse
from menu.models import *
from django.utils import simplejson
# Create your views here.
def get_menuitems_by_menu(request):
	if request.is_ajax():
		l = []
		menu_id  = request.GET['menu_id']
		if menu_id:
			menuitems = MenuItem.objects.filter(menu = int(menu_id))

			for item in menuitems:
				i = {}
				if item.get_level() == 0:
					i['text'] = item.name
				else:
					i['text'] = '---'*item.get_level()+' '+item.name
				i['value'] = item.id
				l.append(i)
		
		return HttpResponse(simplejson.dumps(l),mimetype = 'application/json')
