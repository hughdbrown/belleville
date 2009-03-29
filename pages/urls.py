from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('django.views.generic.simple',
    (r'^resume/$',     'direct_to_template', {'template': 'resume.html'}),
    (r'^about/$',     'direct_to_template', {'template': 'about.html'}),
    (r'^books/$',     'direct_to_template', {'template': 'library.html'}),
    (r'^$',           'direct_to_template', {'template': 'about.html'}),
)

