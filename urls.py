from django.conf.urls.defaults import *
from django.contrib import admin

from belleville.admin import site
from belleville.feeds import LatestDjangoEntries, LatestEntries
from belleville.settings import MEDIA_ROOT

admin.autodiscover()

feeds = {
    'django': LatestDjangoEntries, 
    'all': LatestEntries, 
}

urlpatterns = patterns('',
    url(r'^post/', include('belleville.entry.urls')),
    url(r'^admin/(.*)', site.root),
    url(r'^pages/', include('belleville.pages.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')), 
    url(r'', include('belleville.entry.urls')),
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
