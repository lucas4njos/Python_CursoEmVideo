#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

números = []
def sorteia():
    números.clear()
    for i in range (0, 5):
        números.append(randint(0, 10))
    print(números)

def somaPar(lst):
    soma = 0

    for i in lst:
        if i % 2 ==0:
            soma += i
    print(soma)

sorteia()

somaPar(números)



