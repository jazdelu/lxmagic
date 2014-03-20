from menu.models import Menu

def get_menus(request):
	menus = {}

	for m in Menu.objects.filter(is_active = True):
		menus[m.location] = m



	return menus