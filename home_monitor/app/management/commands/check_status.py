# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from home_monitor.app.models import Log
from home_monitor.app.webserver import getDadosHome

class Command(BaseCommand):
    """docstring for Comand"""

    args = ''
    help = u'''Executa script que pega os dados da home server.'''

    def handle(self, *args, **options):
        
        dados = getDadosHome()
        
        obj_log = Log()
        obj_log.temp_home = dados.get('Home', 0.0)
        obj_log.temp_server = dados.get('PC', 0.0)
        obj_log.temp_hack = dados.get('Hack', 0.0)
        obj_log.tensao_home = dados.get('Voltagem', 0.0)
        obj_log.ip_home = dados.get('Home_IP', '')
        obj_log.is_ok = dados.get('status', False)
        obj_log.save()  

        self.stdout.write(u'Dados Colidos\n')
        self.stdout.write(str(dados))
        self.stdout.write(u'\n')
        self.stdout.write(u'Finalizado\n')
