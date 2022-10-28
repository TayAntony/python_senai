import time
from auxiliar import Auxiliar


def gravar_dados():
    if len(Auxiliar.lista_cadastros) > 0:
        with open('cadastros.txt', 'a') as f:
            for i in Auxiliar.lista_cadastros:
                f.write(str(i) + '\n')
    Auxiliar.lista_cadastros.clear()
    

def rotina():
    while True:
        if not Auxiliar.executar_rotinas:
            break
        time.sleep(2)
        gravar_dados()
        