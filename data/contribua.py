import requests
import requests
from data import ui

def consultar ():
        msg = ('Contibua com esse painel, soluções de erros ou API, para mais modulos de pesquisas e crescimento do painel, entre em contato :)') #meu dc: rickoproprio#1000
        op=int(ui.dialog2(msg))
        if op == 1:
            pass
        elif op ==2:
            Sair=True
        else:
            ui.error()