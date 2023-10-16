#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

lista_final = []
palpites = []
random_num = 0

from random import randint

jogos = int(input('Quantos jogos você deseja sortear? : '))

for c in range(0, jogos):

    for i in range(0, 6):
        while True:
            random_num = randint(0, 60)
            if random_num not in palpites:
                palpites.append(random_num)
                break

    palpites.sort()

    lista_final.append(palpites[:])
    palpites.clear()

print('-*' * 50)

for c in range(0, jogos):
    print(lista_final[c])