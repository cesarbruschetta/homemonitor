# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from home_monitor.settings import LOGIN_URL

#@login_required(login_url=LOGIN_URL)
def home(request):
    """ Home Page """
    context = {}
    
    return render_to_response('home.html', context,
        context_instance=RequestContext(request))
    
    
    
#http://bradmontgomery.blogspot.com.br/2009/04/restricting-access-by-group-in-django.html    
    
    
from chartit import DataPool, Chart

def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    #http://blog.bixly.com/post/14986471657/django-chartit-interactive-charting-django-app
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': [{'month':1,
                            'houston_temp':20,
                            'boston_temp':21},
                          {'month':2,
                            'houston_temp':23,
                            'boston_temp':24},
                          {'month':3,
                            'houston_temp':23,
                            'boston_temp':25},
                          {'month':4,
                            'houston_temp':27,
                            'boston_temp':24}]},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('chart.html',{'weatherchart': cht})



    