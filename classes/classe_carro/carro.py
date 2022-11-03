import inquirer
from carro import Carro, Veiculo, Menu
from carro import Ia

#colocar formula de velocidade por distancia para obter tempo de viagem
#consertar abastecimento que pede o argumento carro
#criar fórmula de gasolina por km/l
#arrumar os erros do valor na carteira para não ser negativo

marca_opcoes = [
        inquirer.List(
            'escolha',
            message = 'MARCA DO CARRO',
            choices = ('Toyota', 'Chevrolet', 'Ford', 'Fiat', 'Volkswagen')
        )
    ]
marca = inquirer.prompt(marca_opcoes)['escolha']

marcas_modelos_correspondentes = {
    'Toyota': ('Corolla',  'RAV4', 'Hilux', 'Camry', 'Prius'),
    'Chevrolet': ('Camaro', 'Cruze', 'Onix', 'Tracker', 'Spin'),
    'Ford': ('Ka', 'Ranger', 'Fiesta', 'Ecosport', 'Edge'),
    'Fiat': ('Mobi', 'Argo', 'Pulse', 'Cronos', 'Fiorino'),
    'Volkswagen': ('Polo', 'Jeta', 'Gol', 'Voyage', 'Fox')
}

opcoes_modelo = [
        inquirer.List(
            'escolha',
            message = 'ESCOLHA O MODELO',
            choices = marcas_modelos_correspondentes[marca]
        )
    ]
    
modelo_escolhido = inquirer.prompt(opcoes_modelo)['escolha']

placa = input('Digite a placa do carro: ').upper()

opcoes_carro = [
    inquirer.List(
        'consumo',
        message = 'CONSUMO DO CARRO (km/L)',
        choices = ('8km/L', '10km/L', '13km/L', '15km/L', '18km/L', '20km/L', '22km/L', '25km/L')
    ),
    inquirer.List(
        'tanque',
        message = 'LITROS DO TANQUE',
        choices = (25, 30, 35, 40, 50)
    ),
    inquirer.List(
        'categoria',
        message = 'CATEGORIA DO CARRO',
        choices = ('Hatch', 'Sedan', 'SUV', 'Pick-up')
    ),
    inquirer.List(
        'airbag',
        message = 'QUANTIDADE DE AIRBAGS',
        choices = (1, 2, 3, 4)
    ),
    inquirer.List(
        'porta_mala',
        message = 'QUANTIDADE DE LITROS NO PORTA MALA',
        choices = (150, 200, 250, 300, 400, 500, 700)
    ),
    inquirer.List(
        'conversivel',
        message = 'CONVERSÍVEL?',
        choices = ('SIM', 'NÃO')
    )
]

escolhas_carro = inquirer.prompt(opcoes_carro)


carro = Carro(
    marca=marca, modelo=modelo_escolhido,
    placa=placa, consumo=escolhas_carro['consumo'],
    nivelCombustivel=escolhas_carro['tanque'],
    categoria=escolhas_carro['categoria'],
    airbags=escolhas_carro['airbag'],
    litrosPortaMala=escolhas_carro['porta_mala'],
    conversivel=escolhas_carro['conversivel']
)

carro.resumo_carro()

cidades = ['Campinas', 'Valinhos', 'Hortolândia', 'Sumaré', 'Vinhedo']

cidades_kilometragem = {
    'Campinas': 100,
    'Valinhos': 50,
    'Hortolândia': 150,
    'Sumaré': 200,
    'Vinhedo': 0
}

saida_opcoes = [
        inquirer.List(
            'escolha',
            message = 'CIDADE ATUAL',
            choices = cidades
        )
    ]
cidade_saida = inquirer.prompt(saida_opcoes)['escolha']
kilometragem_cidade_saida = cidades_kilometragem[cidade_saida]
cidades.remove(cidade_saida)

destino_opcoes = [
        inquirer.List(
            'escolha',
            message = 'CIDADE DESTINO',
            choices = cidades
        )
    ]
    
cidade_chegada = inquirer.prompt(destino_opcoes)['escolha']
kilometragem_cidade_chegada = cidades_kilometragem[cidade_chegada]


distancia_cidades = kilometragem_cidade_saida - kilometragem_cidade_chegada
print(f'A distância das cidades é de {distancia_cidades}km')

ia = Ia(distancia=distancia_cidades, running=False, velocidade=0)

jogo = Menu(carro=carro, ia=ia)
jogo.start()
