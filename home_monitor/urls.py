# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'home_monitor.app.views.home', name='home'),
    
     url(r'^teste/$', 'home_monitor.app.views.weather_chart_view', name='teste'),
    
    # url(r'^home_monitor/', include('home_monitor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Autenticação
    url(r'^login/$', 'django.views.generic.simple.redirect_to', {'url': '/login/google-oauth2/'}, name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout_then_login',name='logout'),
    
    url(r'', include('social_auth.urls')),
    
)
#gambiarra para servir arquivos estaticos
urlpatterns += staticfiles_urlpatterns()
