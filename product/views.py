from django.shortcuts import render_to_response
from django.template import RequestContext


def get_products(request):
	products = [1,1,1,1]
	return render_to_response('list.html',{'products':products},context_instance=RequestContext(request))

def get_product_by_id(request,pid):
	return render_to_response('detail.html',context_instance=RequestContext(request))	
