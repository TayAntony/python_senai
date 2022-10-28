from concurrent.futures import thread
import threading
from auxiliar import Auxiliar
from worker import rotina

Auxiliar.executar_rotinas = True
thread1 = threading.Thread(target=rotina).start()

while True:
    nome = input('digite seu nome: ')
    if nome == "":
        Auxiliar.executar_rotinas = False
        break
    Auxiliar.lista_cadastros.append({'nome': nome})
    