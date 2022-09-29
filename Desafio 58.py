#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

pc = randint(1, 10)
player = 11

while pc != player:
    player = int(input('Digite um número de 1 a 10: '))
    if player == pc:
        print('Você acertou, parabéns!')
    else:
        print('Tente novamente.')