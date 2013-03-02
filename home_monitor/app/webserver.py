# -*- coding: utf-8 -*-
from django.conf import settings

import socket, httplib, urllib

HOST_LOG = getattr(settings, 'URL_HOME_SERVER')
URI_LOG = getattr(settings, 'URI_HOME_SERVER')
PORT_LOG = getattr(settings, 'PORT_HOME_SERVER')

def consultWebService(D={}, HOST=HOST_LOG, URI=URI_LOG, PORT=PORT_LOG, protocol='http' ):
    '''
    Metodo que consulta o webservice
    @D = Dicionario com os parametos para o webservice 
    '''

    valor = {}
    params = urllib.urlencode(D)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    
    C_HOST = '%s:%s' %(HOST,PORT)
    
    try:
        if protocol == 'http':
            conn = httplib.HTTPConnection(C_HOST)
        else:
            conn = httplib.HTTPSConnection(C_HOST)

        conn.request("GET",URI, params, headers)
        
        response = conn.getresponse()
        data = response.read()
        if response.status == 200 and data:
            try:
                valor = eval(data.replace('\r' ,'').replace('\n' ,''))
                valor['status'] = True 
            except:
                valor = {}
                valor['status'] = False

        conn.close()
        
        valor['Home_IP'] = socket.gethostbyname(HOST)
        
    except socket.gaierror:
        valor['status'] = False
        valor['Home_IP'] = ''
    
    return valor


def getDadosHome():
    dados = consultWebService()
    return dados
