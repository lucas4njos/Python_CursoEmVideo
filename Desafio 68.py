#Exercício Python 068: Faça um programa que jogue par ou
# ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
vitoria = 0
from random import randint
while True:
    print('*-'*25)
    escolha = str(input('Par ou Ímpar? -->  ')).strip().upper()[0]

    jogador = int(input('Jogador: '))
    pc = randint(0, 10)

    jogada = jogador+pc

    print(f'PC = {pc} e JOGADOR = {jogador}')

    if escolha == 'P':
        if jogada % 2 == 0:
            vitoria += 1
            print('Você venceu!')
        else:
            print(f'Nessa o computador foi melhor! Você venceu {vitoria} vezes.')
            break
    elif escolha == 'I':
        if jogada % 2 == 0:
            print(f'Nessa o computador foi melhor! Você venceu {vitoria} vezes.')
            break
        else:
            vitoria += 1
            print('Você venceu!')
