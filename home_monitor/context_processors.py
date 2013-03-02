# -*- encoding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site


def get_Site():
    return 'Green Home Monitor'
    #current_site = Site.objects.get_current()
   # return current_site.name



def context(request):
    
    contexto = {
        'current_absolute_url': request.build_absolute_uri(),
        'static_absolute_url': request.build_absolute_uri(settings.MEDIA_URL),
        'current_path':request.path,
        'website_title':get_Site
        }
    
    
    return contexto