from django.conf.urls import patterns, url
from frontend import views

__author__ = 'niels-ole'

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^order/$', views.order, name='order'),
    url(r'^success/$', views.success, name='success'),
    )