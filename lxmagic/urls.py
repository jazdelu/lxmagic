from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lxmagic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^product/', include('product.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^ajax/menuitem/', 'menu.views.get_menuitems_by_menu',name = 'get_menuitems_by_menu'),
    url(r'^ajax/category/', 'product.views.get_category_url',name = 'get_category_url'),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
