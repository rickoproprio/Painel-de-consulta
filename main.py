import os, sys

from data import contribua
#rick anda codando aqui
def restart():
	python=sys.executable;os.excl(python, python, *sys.argv)
try:
	import colorama, requests
except:
	os.system('pip install -r requirements.txt');restart()
try:
	from data import ui, cep, cpf, cnpj, telefone, contribua
except Exception as e:
	print('falha no sistema kk '+str(e));exit()
C= "\033[97;1m"
G = "\033[92;1m"
P = "\033[1;35m"
Sair=False
while(Sair==False):
	try:
		op=int(ui.menu(ms0=f'\n{C}[{G}1{C}] CEP\n{C}[{G}2{C}] CPF (OFF)\n{C}[{G}3{C}] CNPJ\n{C}[{G}4{C}] TELEFONE (OFF)\n{C}[{G}5{C}] Futuramente mais consultas xD\n{C}[{P}0{C}] Sair'))
		if op==1:
			cep.consultar()
		elif op==2:
			cpf.consultar()
		elif op==3:
			cnpj.consultar()
		elif op==4:
			telefone.consultar()
		elif op==5:
			contribua.consultar()
		elif op==0:
			ui.clear();Sair=True
	except:
		ui.error()
