from django.conf.urls.defaults import *
from django.contrib import admin

from belleville.admin import site
from belleville.feeds import LatestDjangoEntries, LatestEntries

admin.autodiscover()

feeds = {
    'django': LatestDjangoEntries, 
    'all': LatestEntries, 
}

urlpatterns = patterns('',
    (r'^post/', include('belleville.entry.urls')),
    (r'^admin/(.*)', site.root),
    (r'^pages/', include('belleville.pages.urls')),
    (r'^comments/', include('django.contrib.comments.urls')), 
    (r'', include('belleville.entry.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/barbara/Code/belleville/site_media/'}),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

