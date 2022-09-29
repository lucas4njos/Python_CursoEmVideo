#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

a = 0

while a < 10:
    print(f'{primeiro_termo}', end=' - ')
    primeiro_termo += razao
    a += 1