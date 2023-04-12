import requests
from data import ui
def consultar():
	Sair=False
	while (Sair==False):
		cnpj = int(ui.dialog1())
		r = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}').text
		if 'Request retornada com sucesso' in r:
			msg='Deculpe Não consegui retornar a sua request.'
		else:
			msg=r.replace('<p>', '').replace('<br>', '\n')
		op=int(ui.dialog2(msg))
		if op ==1:
			pass
		elif op==2:
			Sair=True
		else:
			ui.error()