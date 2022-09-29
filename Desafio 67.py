#Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('\nDigite um número: '))
    if num < 0:
        break
    for i in range (0, 10):
        print(f'{i+1} * {num} = {(i+1) * num}', end= ' | ')
print('Programa encerrado!')
