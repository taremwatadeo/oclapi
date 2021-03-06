from django.conf.urls import patterns, url
from mappings.views import MappingListView, MappingDetailView

__author__ = 'misternando'

urlpatterns = patterns('',
    url(r'^$', MappingListView.as_view(), name='mapping-list'),
    url(r'^(?P<mapping>[a-zA-Z0-9\-\.]+)/$', MappingDetailView.as_view(), name='mapping-detail'),
)
