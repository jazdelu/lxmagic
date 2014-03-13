from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def get_news(request):
	news = [1,1]
	return render_to_response('news.html',{"news":news},context_instance=RequestContext(request))	