from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travel_buddy/$', views.logged_in),
    url(r'^travel_buddy/new/$', views.new),
    url(r'^travel_buddy/show/(?P<id>\d+)$', views.show),
    url(r'^create$', views.create), 
    url(r'^delete/(?P<id>\d+)$', views.destroy),
    url(r'^logout/$', views.logout),
    url(r'^join/(?P<id>\d+)/$', views.join),
    url(r'^cancel/(?P<id>\d+)/$', views.cancel),
]