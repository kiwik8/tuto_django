from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing, name='list'),
    url(r'^(?P<variety_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search),
]