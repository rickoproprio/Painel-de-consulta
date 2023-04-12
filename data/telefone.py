import requests
import requests
from data import ui

def consultar ():
        msg = ('Olá, essa consulta de telefone está temporariamente fora do ar, por motivos que a API expirou, se você tem APis e quer continunar o projeto entre em contato') #meu dc rickoproprio#1000
        op=int(ui.dialog2(msg))
        if op == 1:
            pass
        elif op ==2:
            Sair=True
        else:
            ui.error()