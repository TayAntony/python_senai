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


class Ia:
    running = True
    distancia = 0
    velocidade = 0


class Menu():
    carteira = 500
    def menu(opcao):
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'MENU DE OPÇÕES',
            choices = ('Acelerar', 'Desacelerar', 'Manutenir', 'Finanças', 'Sair')
            )
        ]

        respostas = inquirer.prompt(opcoes)

        if respostas['escolha'] == 'Acelerar':
            Menu.acelerar(opcao)

        elif respostas['escolha'] == 'Desacelerar':
            Menu.desacelerar(opcao)
        
        elif respostas['escolha'] == 'Manutenir':
            Menu.manutenir(opcao)

        elif respostas['escolha'] == 'Finanças':
            Menu.financas(opcao)

        elif respostas['escolha'] == 'Sair':
            Menu.sair(opcao)
        
        return opcoes
        
    def acelerar(opcao, carteira):
        Ia.velocidade+= 10
        print('Sua velocidade foi aumentada em 10km/h')
        print(f'Velocidade atual: {Ia.velocidade}')
        if Ia.velocidade >= 80:
            print('Atenção! Velocidade máxima permitida na rodovia.')
            if Ia.velocidade > 90:
                print('Você recebeu uma multa de R$50,00 por excesso de velocidade!')
                carteira -= 50

    def desacelerar(opcao):
        Ia.velocidade-= 10
        if Ia.velocidade == 0:
            print('A velocidade já está em 0km/h!')
        else:
            print('Sua velocidade foi reduzida em 10km/h')
            print(f'Velocidade atual: {Ia.velocidade}')

    def manutenir(opcao, carteira):
        
        mecanico = ['Trocar pneus - R$300,00', 'Trocar óleo - R$50,00', 'Lavagem completa - R$150,00', 'Calibragem - R$30,00', 'Voltar']
        valores = [300, 50, 150, 30, 0]
        print('Indo ao mecânico!')
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'MECÂNICO',
            choices = mecanico
            )
        ]

        respostas = inquirer.prompt(opcoes)

        if respostas['escolha'] == 'Trocar pneus':
            if valores[0] > carteira:
                print('Valor insuficiente na carteira para efetuar pagamento!')
            else:
                print('Pagamento efetuado com sucesso! Aproveite os novos pneus')
                carteira -= valores[0]
            print(f'Valor na carteira: R$ {carteira},00')

        elif respostas['escolha'] == 'Trocar óleo':
            if valores[1] > carteira:
                print('Valor insuficiente na carteira para efetuar pagamento!')
            else:
                print('Pagamento efetuado com sucesso! Aproveite o novo óleo')
                carteira -= valores[1]
            print(f'Valor na carteira: R$ {carteira},00')
        
        elif respostas['escolha'] == 'Lavagem completa':
            if valores[2] > carteira:
                print('Valor insuficiente na carteira para efetuar pagamento!')
            else:
                print('Pagamento efetuado com sucesso! Aproveite a lavagem')
                carteira -= valores[2]
            print(f'Valor na carteira: R$ {carteira},00')

        elif respostas['escolha'] == 'Calibragem':
            if valores[3] > carteira:
                print('Valor insuficiente na carteira para efetuar pagamento!')
            else:
                print('Pagamento efetuado com sucesso! Aproveite a calibragem')
                carteira -= valores[3]
            print(f'Valor na carteira: R$ {carteira},00')

        elif respostas['escolha'] == 'Voltar':
            Menu.menu()

    def financas(opcao, carteira):
        opcoes = [
        inquirer.List(
            'escolha',
            message = 'SUA CARTEIRA',
            choices = ('Saldo', 'Adicionar dinheiro', 'Sacar', 'Voltar')
            )
        ]

        respostas = inquirer.prompt(opcoes)

        if respostas['escolha'] == 'Saldo':
            print(f'Valor na carteira: R$ {carteira},00')

        elif respostas['escolha'] == 'Adicionar dinheiro':
            add = input('Digite o valor que quer adicionar: R$')
            carteira += add
            print('Valor adicionado com sucesso!')

        elif respostas['escolha'] == 'Sacar':
            saque = input('Digite o valor que quer sacar: R$')
            carteira -= saque
            print('Valor sacado com sucesso!')

        elif respostas['escolha'] == 'Voltar':
            Menu.menu()

    def sair(opcao):
        sys.exit()
        