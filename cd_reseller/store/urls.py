from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.listing, name='listing'),
    url(r'^(?P<variety_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
]