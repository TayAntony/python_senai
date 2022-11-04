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
\033[1;34mConsumo (km/L):\033[0;0m \033[1;32m{self.consumo}km/L\033[0;0m
\033[1;34mTanque:\033[0;0m \033[1;32m{self.nivelCombustivel} L\033[0;0m
\033[1;34mCategoria:\033[0;0m \033[1;32m{self.categoria}\033[0;0m
\033[1;34mQuantidade Airbags:\033[0;0m \033[1;32m{self.airbags}\033[0;0m
\033[1;34mPorta-mala (l):\033[0;0m \033[1;32m{self.litrosPortaMala}\033[0;0m
\033[1;34mConversível?\033[0;0m \033[1;32m{self.conversivel}\033[0;0m
''')


class Ia:
    def __init__(self, running, distancia, velocidade, consumo):
        self.running = running
        self.distancia = distancia
        self.velocidade = velocidade
        self.distancia_inicial = 0
        self.consumo = consumo
        #self.abastecendo = abastecendo

    def calculo_tempo(self):
        if self.velocidade > 0:
            self.running = True

            if self.distancia < 0:
                self.distancia *= 1
            else:
                tempo = (self.distancia/self.velocidade)*60
                print(f'\033[34mA viagem demorará {tempo:.2f} minutos\033[0;0m')

#arrumar vínculo de velocidade por distancia
                if self.running == True:
                    self.distancia_inicial += 10
                    print(f'O destino está a {self.distancia-self.distancia_inicial}km de distância')
                else:
                    self.distancia_inicial -= 10
                    print(f'O destino está a {self.distancia+self.distancia_inicial}km de distância')

            if self.distancia_inicial == self.distancia:
                print('\033[2mVocê chegou ao seu destino... \033[0;0m🏁')
                #self.gasto_combustivel()
                sys.exit()
                
        else:
            self.running = False
            print('O carro está parado...')
        
    #def gasto_combustivel(self):
        #passar o parametro 'abastecendo' da classe menu para a classe ia para calcular o gasto de combustivel por km rodado
        # gasto_gasolina = self.distancia/self.consumo
        # if self.abastecendo == 0 or self.abastecendo < gasto_gasolina:
        #     print('Seu carro precisa abastecer, vá ao posto')
        # else:
        #     print(f'Seu carro gastou {gasto_gasolina:.1f} litros de gasolina nessa viagem')


class Menu():
    def __init__(self, carro:Carro, ia:Ia, nivelCombustivel):
        self.carro = carro
        self.ia = ia
        self.carteira = 500
        self.nivelCombustivel = nivelCombustivel
        self.abastecendo = 0


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
        self.ia.running = True
        self.ia.velocidade += 10
        print('\033[32mSua velocidade foi aumentada em 10km/h\033[0;0m')
        print(f'Velocidade atual: {self.ia.velocidade}km/h')
        if self.ia.velocidade > 80:
            print('\033[31mAtenção! Você está na velocidade máxima permitida na rodovia. CUIDADO\033[0;0m')
        self.ia.calculo_tempo()
        self.menu()


    def desacelerar(self):
        self.ia.running = False
        if self.ia.velocidade == 0:
            self.ia.running = False
            print('\033[34mA velocidade já está em 0km/h!\033[0;0m')
        else:
            self.ia.velocidade -= 10
            print('\033[33mSua velocidade foi reduzida em 10km/h\033[0;0m')
            print(f'Velocidade atual: {self.ia.velocidade}')
        self.ia.calculo_tempo()
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
            print('\033[31mValor insuficiente na carteira para efetuar pagamento!\033[0;0m')
        else:
            print('\033[32mPagamento efetuado com sucesso!\033[0;0m')
            self.carteira -= valor
            print(f'Valor na carteira: R$ {self.carteira}')
        self.ia.calculo_tempo()
        self.menu()


    def abastecer(self):
        
        self.ia.running = False
        print('BEM-VINDO AO POSTAY ABASTECIMENTOS')
        print('>>> R$3,50L')

        litros_abastecer = [
            inquirer.List(
            'abastecer',
            message = 'ESCOLHA A QUANTIDADE DE LITROS',
            choices = (2, 4, 5, 8, 10, 15)
        )]
        escolha = inquirer.prompt(litros_abastecer)['abastecer']
        
        valor_abastecimento = escolha*3.50 
        print(f'Você quer abastecer {escolha} litros, valor total: R${valor_abastecimento}')
        if self.carro.nivelCombustivel > escolha:
            if self.carteira > valor_abastecimento:
                self.abastecendo += escolha
                if self.abastecendo > self.carro.nivelCombustivel:
                    print('\033[34mSeu tanque está quase cheio, abasteça menos!\033[0;0m')
                else:
                    self.carteira -= valor_abastecimento
                    print('\033[32mAbastecido com sucesso\033[0;0m')
                    print(f'\033[32mSeu tanque tem {self.abastecendo} litros de gasolina\033[0;0m')
                self.menu()
            else:
                print('\033[31mSaldo insuficiente na carteira, abasteça menos ou aumente seu saldo\033[0;0m')
                self.menu()
        self.ia.calculo_tempo()


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
            print(f'\033[32mValor na carteira: R$ {self.carteira}\033[0;0m')

        elif escolha == 'Adicionar dinheiro':
            add = int(input('Digite o valor que quer adicionar: R$'))
            self.carteira += add
            print('\033[32mValor adicionado com sucesso!\033[0;0m')

        elif escolha == 'Sacar':
            saque = int(input('Digite o valor que quer sacar: R$'))
            self.carteira -= saque
            print('\033[32mValor sacado com sucesso!\033[0;0m')

        self.menu()


    def sair(self):
        print('\033[35mAté o próximo código Lulu \033[0;0m👋')
        sys.exit()
        
