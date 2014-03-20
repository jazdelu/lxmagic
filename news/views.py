from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import News
# Create your views here.
def get_news(request):
	news = News.objects.all()
	return render_to_response('news.html',{"news":news},context_instance=RequestContext(request))	