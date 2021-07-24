from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.listing, name='listing'),
    url(r'^(?P<variety_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^booking/(?P<variety_id>[0-9]+)/$', views.booking, name='booking')

]
