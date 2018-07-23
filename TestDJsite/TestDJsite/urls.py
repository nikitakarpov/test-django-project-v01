"""TestDJsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from firstApp import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^firstapp/', include('firstApp.urls')),
    re_path(r'^', include('mainpage.urls')),
    re_path(r'^front-test-1/', include('front_test_1.urls')),
    #re_path(r'^blog/', include('blog.urls'))
    re_path(r'^test_request/', views.test_request),
    re_path(r'^mailtest/', views.mailtest),
    re_path(r'^contact/thanks/', views.contact_thanks),
    re_path(r'^contact2/', views.contact),
    re_path(r'^contact3/', views.contact3)
]