#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(num):
    return(num+1)
def diminuir(num):
    return(num-1)
def dobro(num):
    return(num*2)
def metade(num):
    return(num/2)
def linha():
    print('*-' * 25)
def moeda(num):
    return(f'R${num:.2f}')