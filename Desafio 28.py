# Exercício Python 028: Escreva um programa que faça o computador
# "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

usuario = int(input("Digite um número entre 0 e 5: "))
pc = randint(0, 5)


print("\n\033[34:1mPROCESSANDO...")
sleep(2)
print("QUASE LÁ...\033[m")
sleep(2)
print(f"O número escolhido foi {pc}.")

if pc == usuario:
    print("VOCÊ VENCEU!")
else:
    print("VOCÊ PERDEU!")

