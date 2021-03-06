from django.shortcuts import render_to_response
from django.template import RequestContext
from product.models import Product, Category
from django.http import Http404,HttpResponse
def get_products(request):
	products = Product.objects.all()
	return render_to_response('list.html',{'products':products,},context_instance=RequestContext(request))

def get_product_by_id(request,pid):
	product = ''
	try:
		product = Product.objects.get(id = pid)
	except Product.DoesNotExist:
		raise Http404
	products = list(Product.objects.all())
	i = products.index(product)
	next_p =''
	prev_p =''
	if len(products)>1:
		if (i == 0):
			next_p = products[i+1]
		elif (i == len(products)-1):
			prev_p = products[i-1]
		else:
			next_p = products[i+1]
			prev_p = products[i-1]
	else:
		pass
	return render_to_response('detail.html',{'product':product,'next_p':next_p,'prev_p':prev_p},context_instance=RequestContext(request))	

def get_products_by_category(request,hierarchy):
	slugs = filter(None,hierarchy.split('/'))
	print slugs
	category =''
	products = []
	query_c = []
	try: 
		category = Category.objects.get(slug = slugs[-1])
		for c in category.get_descendants(include_self=True):
			query_c.append(c)

	except:
		pass

	if category:
		products = Product.objects.filter(category__in = query_c)

	return render_to_response('list.html',{'products':products,'category':category},context_instance=RequestContext(request))

def get_category_url(request):
	url=''
	if request.is_ajax():
		if request.GET['cid']:
			url = 'http://'	
			if int(request.GET['cid']) > 0:
				url += Category.objects.get(id = request.GET['cid']).get_url
			else:
				pass
		else:
			pass
	return HttpResponse(url,mimetype = 'application/text')



		