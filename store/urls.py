from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^cum_cumperi$', views.cum_cumperi, name='cum_cumperi'),
    url(r'^cumparam$', views.cumparam, name='cumparam'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^(?P<pk>[^/]+)/(?P<id>\d+)/$', views.book_details, name='book_details'),
    url(r'^(?P<pk>[^/]+)/$', views.category_search, name='category_search'),

]
