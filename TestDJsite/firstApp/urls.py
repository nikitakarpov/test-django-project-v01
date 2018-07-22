
from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.hey, name='index'),
    url(r'^date-time/$', views.current_datetime, name='datetime'),
    url(r'^date-time/plus/(\d{1,2})', views.datetime_plus, name='datetime_plus'),
    url(r'^search-form/$', views.search, name='search')
]