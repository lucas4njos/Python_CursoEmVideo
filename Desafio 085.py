#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em
# uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e
# ímpares em ordem crescente.

numeros = []
main_list = []

for i in range(0, 7):
    num = int(input('Digite um número: '))
    numeros.append(num)

print('*-' * 50)

print(numeros)

print(f'\nNúmeros pares: ', end = '')
for i in range(0, 7):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=',')

print(f'\nNúmeros ímpares: ', end = '')
for i in range(0, 7):
    if numeros[i] % 2 != 0:
        print(numeros[i], end=',')
