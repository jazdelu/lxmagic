from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import News
from django.http import Http404
# Create your views here.
def get_news(request):
	news = News.objects.all()
	return render_to_response('news.html',{"news":news},context_instance=RequestContext(request))


def get_news_by_id(request, nid):
	news = ''
	try:
		news = News.objects.get(id = nid)
	except:
		raise Http404
	return render_to_response('news_detail.html',{"news":news},context_instance=RequestContext(request))