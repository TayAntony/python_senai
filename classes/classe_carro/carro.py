import inquirer
import sys

class Veiculo():
    def __init__(self, marca, modelo, placa, consumo, nivelCombustivel):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.consumo = consumo
        self.nivelCombustivel = nivelCombustivel 
   

class Carro(Veiculo):
    def __init__(self, categoria, airbags, litrosPortaMala, conversivel, marca, modelo, placa, consumo, nivelCombustivel):
        super().__init__(marca, modelo, placa, consumo, nivelCombustivel)
        self.categoria = categoria
        self.airbags = airbags
        self.litrosPortaMala = litrosPortaMala
        self.conversivel = conversivel

    def resumo_carro(self):
        print(f'''
\033[1;34mMarca:\033[0;0m \033[1;32m{self.marca}\033[0;0m
\033[1;34mModelo:\033[0;0m \033[1;32m{self.modelo}\033[0;0m
\033[1;34mPlaca:\033[0;0m \033[1;32m{self.placa}\033[0;0m
\033[1;34mConsumo (km/L):\033[0;0m \033[1;32m{self.consumo}\033[0;0m
\033[1;34mTanque:\033[0;0m \033[1;32m{self.nivelCombustivel}\033[0;0m
\033[1;34mCategoria:\033[0;0m \033[1;32m{self.categoria}\033[0;0m
\033[1;34mQuantidade Airbags:\033[0;0m \033[1;32m{self.airbags}\033[0;0m
\033[1;34mPorta-mala (l):\033[0;0m \033[1;32m{self.litrosPortaMala}\033[0;0m
\033[1;34mConversível?\033[0;0m \033[1;32m{self.conversivel}\033[0;0m
''')


class Ia:
    def __init__(self, running, distancia, velocidade):
        self.running = running
        self.distancia = distancia
        self.velocidade = velocidade

    def calculo_tempo():
        pass


class Menu():
    multa = False
    
    def __init__(self, carro, ia):
        self.carro = carro
        self.ia = ia
        self.carteira = 500

    def start(self):
        self.menu()
    
    def menu(self):
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'MENU DE OPÇÕES',
            choices = ('Acelerar', 'Desacelerar', 'Manutenir', 'Finanças', 'Abastecer', 'Sair')
            )
        ]

        respostas = inquirer.prompt(opcoes)

        if respostas['escolha'] == 'Acelerar':
            self.acelerar()

        elif respostas['escolha'] == 'Desacelerar':
            self.desacelerar()
        
        elif respostas['escolha'] == 'Manutenir':
            self.manutenir()

        elif respostas['escolha'] == 'Finanças':
            self.financas()
        
        elif respostas['escolha'] == 'Abastecer':
            self.abastecer()

        elif respostas['escolha'] == 'Sair':
            self.sair()
            
            
    def acelerar(self):
        
        self.ia.velocidade += 10
        print('Sua velocidade foi aumentada em 10km/h')
        print(f'Velocidade atual: {self.ia.velocidade}km/h')
        if self.ia.velocidade > 80:
            print('Atenção! Você está na velocidade máxima permitida na rodovia. CUIDADO')
        self.menu()


    def desacelerar(self):
        if self.ia.velocidade == 0:
            print('A velocidade já está em 0km/h!')
        else:
            self.ia.velocidade -= 10
            print('Sua velocidade foi reduzida em 10km/h')
            print(f'Velocidade atual: {self.ia.velocidade}')
        self.menu()


    def manutenir(self):
        print('Indo ao mecânico!')
        opcoes_mecanico = [
            'Trocar pneus - R$300,00', 
            'Trocar óleo - R$50,00', 
            'Lavagem completa - R$150,00', 
            'Calibragem - R$30,00', 'Voltar'
        ]
        
        valores = {
            'Trocar pneus - R$300,00': 300,
            'Trocar óleo - R$50,00': 50,
            'Lavagem completa - R$150,00': 150,
            'Calibragem - R$30,00': 30, 
            'Voltar': 0
        }
        
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'MECÂNICO',
            choices = opcoes_mecanico
            )
        ]

        escolha = inquirer.prompt(opcoes)['escolha']

        if escolha == 'Voltar':
            return self.menu()

        valor = valores[escolha]
        if valor > self.carteira:
            print('Valor insuficiente na carteira para efetuar pagamento!')
        else:
            print('Pagamento efetuado com sucesso!')
            self.carteira -= valor
            print(f'Valor na carteira: R$ {self.carteira},00')
        
        self.menu()

    def abastecer(self, carro:Carro):
        print('BEM-VINDO AO POSTAY ABASTECIMENTOS')
        print('>>> R$3,50l')

        litros_abastecer = [
            inquirer.List(
            'abastecer',
            message = 'ESCOLHA A QUANTIDADE DE LITROS',
            choices = (2, 4, 5, 8, 10, 15)
        )]
        escolha = inquirer.prompt(litros_abastecer)['abastecer']

        valor_abastecimento = escolha*3.50 
        print(f'Você quer abastecer {escolha} litros, valor total: R${valor_abastecimento}')
        if carro.nivelCombustivel > escolha:
            if self.carteira > valor_abastecimento:
                self.carteira -= valor_abastecimento
                carro.nivelCombustivel += escolha
                print('Abastecido com sucesso')
                self.menu()
            else:
                print('Saldo insuficiente na carteira, abasteça menos ou aumente seu saldo')
                self.menu()
        else:
            print('Seu tanque está quase cheio, abasteça menos')
            self.menu()

    def financas(self):
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'SUA CARTEIRA',
            choices = ('Saldo', 'Adicionar dinheiro', 'Sacar', 'Voltar')
            )
        ]

        escolha = inquirer.prompt(opcoes)['escolha']

        if escolha == 'Saldo':
            print(f'Valor na carteira: R$ {self.carteira},00')

        elif escolha == 'Adicionar dinheiro':
            add = int(input('Digite o valor que quer adicionar: R$'))
            self.carteira += add
            print('Valor adicionado com sucesso!')

        elif escolha == 'Sacar':
            saque = int(input('Digite o valor que quer sacar: R$'))
            self.carteira -= saque
            print('Valor sacado com sucesso!')

        self.menu()

    def sair(self):
        sys.exit()
        
