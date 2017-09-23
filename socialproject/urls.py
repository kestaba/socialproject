# -*- coding: utf-8 -*-

"""socialproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# Vista genérica que nos muestra un template con el mensaje "Inicia sesión con facebook"
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views


urlpatterns = [

    # Login URL
    url(r'^login/$', auth_views.login, name='login'),

    # Logout URL
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='user-logout'),

    # Python Social Auth URLs
    url('', include('social_django.urls', namespace='social')),

    # Home URL
    url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
   
    url(r'^admin/', admin.site.urls),
]
