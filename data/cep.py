import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		cep = int(ui.dialog1())
		r = requests.get(f'https://ws.apicep.com/cep/{cep}.json').text
		if 'Request retornada com sucesso' in r:
			msg='Desculpe, não consegui retornar a sua request.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()