#Exercício Python 062: Melhore o DESAFIO 061, perguntando
# para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
a = 0
continua = 10
while True:
    while a < continua:
        print(f'{primeiro_termo}', end=' - ')
        a += 1
        primeiro_termo += razao
    continua = int(input('Deseja mais quantos termos?'))
    a = 0
    if continua == 0:
        break