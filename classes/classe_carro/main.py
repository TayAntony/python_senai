import threading
import inquirer
from carro import Carro, Veiculo, Menu
from resumo_carro import Resumo
from carro import Ia
from att import Exibir

marca = [
        inquirer.List(
            'escolha',
            message = 'MARCA DO CARRO',
            choices = ('Toyota', 'Chevrolet', 'Ford', 'Fiat', 'Volkswagen')
        )
    ]
respostas_marca = inquirer.prompt(marca)

if respostas_marca['escolha'] == 'Toyota':
    modelo = [
        inquirer.List(
            'escolha',
            message = 'MODELOS DO TOYOTA',
            choices = ('Corolla', 'RAV4', 'Hilux', 'Camry', 'Prius')
        )
    ]
    respostas_modelo = inquirer.prompt(modelo)

elif respostas_marca['escolha'] == 'Chevrolet':
    modelo = [
        inquirer.List(
            'escolha',
            message = 'MODELOS DO CHEVROLET',
            choices = ('Camaro', 'Cruze', 'Onix', 'Tracker', 'Spin')
        )
    ]
    respostas_modelo = inquirer.prompt(modelo)

elif respostas_marca['escolha'] == 'Ford':
    modelo = [
        inquirer.List(
            'escolha',
            message = 'MODELOS DA FORD',
            choices = ('Ka', 'Ranger', 'Fiesta', 'Ecosport', 'Edge')
        )
    ]
    respostas_modelo = inquirer.prompt(modelo)

elif respostas_marca['escolha'] == 'Fiat':
    modelo = [
        inquirer.List(
            'escolha',
            message = 'MODELOS DA FORD',
            choices = ('Mobi', 'Argo', 'Pulse', 'Cronos', 'Fiorino')
        )
    ]
    respostas_modelo = inquirer.prompt(modelo)

elif respostas_marca['escolha'] == 'Volkswagen':
    modelo = [
        inquirer.List(
            'escolha',
            message = 'MODELOS DA VOLKSWAGEN',
            choices = ('Polo', 'Jeta', 'Gol', 'Voyage', 'Fox')
        )
    ]
    respostas_modelo = inquirer.prompt(modelo)

placa = input('Digite a placa do carro: ').upper()

consumo = [
        inquirer.List(
            'escolha',
            message = 'CONSUMO DO CARRO (km/L)',
            choices = ('8km/L', '10km/L', '13km/L', '15km/L', '18km/L', '20km/L', '22km/L', '25km/L')
        )
    ]
respostas_consumo = inquirer.prompt(consumo)

tanque = [
        inquirer.List(
            'escolha',
            message = 'NÍVEL DO TANQUE',
            choices = ('Baixo', 'Médio', 'Alto', 'Reserva')
        )
    ]
respostas_tanque = inquirer.prompt(tanque)

categoria = [
        inquirer.List(
            'escolha',
            message = 'CATEGORIA DO CARRO',
            choices = ('Hatch', 'Sedan', 'SUV', 'Pick-up')
        )
    ]
respostas_categoria = inquirer.prompt(categoria)

airbag = [
        inquirer.List(
            'escolha',
            message = 'QUANTIDADE DE AIRBAGS',
            choices = (1, 2, 3, 4)
        )
    ]
respostas_airbag = inquirer.prompt(airbag)

lPortaMala = [
        inquirer.List(
            'escolha',
            message = 'QUANTIDADE DE LITROS NO PORTA MALA',
            choices = (150, 200, 250, 300, 400, 500, 700)
        )
    ]
respostas_porta_mala = inquirer.prompt(lPortaMala)

convers = [
        inquirer.List(
            'escolha',
            message = 'CONVERSÍVEL?',
            choices = ('SIM', 'NÃO')
        )
    ]
respostas_conversivel = inquirer.prompt(convers)


carro = Resumo(marca=respostas_marca['escolha'], modelo=respostas_modelo['escolha'], placa=placa, consumo=respostas_consumo['escolha'], nivelCombustivel=respostas_tanque['escolha'], categoria=respostas_categoria['escolha'], airbags=respostas_airbag['escolha'], litrosPortaMala=respostas_porta_mala['escolha'], conversivel=respostas_conversivel['escolha'])
carro.resumo_carro()

cidades = ['Campinas', 'Valinhos', 'Hortolândia', 'Sumaré', 'Vinhedo']

cidade_atual = [
        inquirer.List(
            'escolha',
            message = 'CIDADE ATUAL',
            choices = cidades
        )
    ]
respostas = inquirer.prompt(cidade_atual)

if respostas['escolha'] == 0:
    cidade1 = 100

elif respostas['escolha'] == 1:
    cidade1 = 50

elif respostas['escolha'] == 2:
    cidade1 = 150

elif respostas['escolha'] == 3:
    cidade1 = 200

elif respostas['escolha'] == 4:
    cidade1 = 0

cidades.remove(respostas['escolha'])

cidade_destino = [
        inquirer.List(
            'escolha',
            message = 'CIDADE DESTINO',
            choices = cidades
        )
    ]
respostas = inquirer.prompt(cidade_destino)

if respostas['escolha'] == 0:
    cidade2 = 100

elif respostas['escolha'] == 1:
    cidade2 = 50

elif respostas['escolha'] == 2:
    cidade2 = 150

elif respostas['escolha'] == 3:
    cidade2 = 200

elif respostas['escolha'] == 4:
    cidade2 = 0

distancia_cidades = cidade1-cidade2

distancia = Ia(distancia=distancia_cidades)
Ia.velocidade = 80

info = Exibir()
thread1 = threading.Thread(target=info.atualizar).start()
