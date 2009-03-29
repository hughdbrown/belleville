from django.conf.urls.defaults import *
from django.contrib.comments.models import Comment
from django.views.generic.simple import direct_to_template

from belleville.entry import views

urlpatterns = patterns('',
    url(r'^view/(?P<title>.*?)/*$',           views.view,             name='entry_view'),
    url(r'^viewid/(?P<id>\w+)/*$',            views.viewid,           name='entry_viewbyid'),
    url(r'^preview/(?P<title>.*?)/*$',        views.preview,          name='entry_preview'),

    url(r'^all/*$',			      views.list_all,	      name='entry_list_all'),

    url(r'^category/(?P<category>.*?)/*$',    views.list_entries,             name='entry_list'),
    url(r'^author/(?P<username>.*?)/*$',      views.list_entries,             name='entry_list'),
    url(r'^date/(?P<date>.*?)/*$',            views.list_entries,             name='entry_list'),
    url(r'^$',                                views.list_entries,             name='entry_list'),
)
