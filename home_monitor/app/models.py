# -*- coding: utf-8 -*-
from django.db import models
#from django.contrib import admin
from datetime import datetime

class Log(models.Model):
    """Table of the database used to save the data 
        of log of the home monitoring """
    
    temp_home = models.DecimalField("Temperatura da casa", max_digits=4, decimal_places=2)
    temp_server = models.DecimalField("Temperatura do server", max_digits=4, decimal_places=2)
    temp_hack = models.DecimalField("Temperatura do hack", max_digits=4, decimal_places=2)
    tensao_home = models.DecimalField("Tensão da casa", max_digits=4, decimal_places=2)

    date_creation = models.DateTimeField(default=datetime.now())    
    ip_home = models.IPAddressField('IP da casa', null=True)
    is_ok = models.BooleanField('Status da consulta',default=False)

