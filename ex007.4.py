from time import sleep
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
maior = n1
menor = n1

print(f'Analisando os números...')
sleep(1.5)

if n2>maior:
    maior = n2
if n3>maior:
    maior = n3
print(f'O {maior} é o maior')
if n2<n1:
    menor = n2
if n3<n2:
    menor = n3
print(f'O {menor} é o menor')
