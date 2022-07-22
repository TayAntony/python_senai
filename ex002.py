def calcular(valor1, valor2):
    resultado = valor1 + valor2
    print(f'O resultado da soma foi {resultado}')

def subtrair(valor1, valor2):
    resultado = valor1 - valor2
    print(f'O resultado da subtração foi: {resultado}')

def multiplicar(valor1, valor2):
    resultado = valor1 * valor2
    print(f'O resultado da multiplicação foi: {resultado}')

def divisão(valor1, valor2):
    resultado = valor1 / valor2
    print(f'O resultado da divisão foi: {resultado:.2f}')


valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
opcao = int(input('''O que deseja fazer com os valores?
[1] somar
[2] subtrair 
[3] multiplicar
[4] dividir
>>>>>>> Sua opção: '''))

if opcao == 1:
    calcular(valor1, valor2)
elif opcao == 2:
    subtrair(valor1, valor2)
elif opcao == 3:
    multiplicar(valor1, valor2)
elif opcao == 4:
    divisão(valor1, valor2)
