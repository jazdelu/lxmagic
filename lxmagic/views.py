from django.shortcuts import render_to_response
from django.template import RequestContext
from banner.models import Banner
def home(request):

	banners = Banner.objects.all()

	return render_to_response('index.html',{'banners':banners},context_instance=RequestContext(request))
