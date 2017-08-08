"""tucao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from usermanage import views as usermanage_views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',usermanage_views.index,name='home'),
    url(r'^regist/$',usermanage_views.regist,name='regist'),
    url(r'^login/$',usermanage_views.login,name='login'),
]
