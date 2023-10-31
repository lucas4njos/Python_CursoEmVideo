#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = 1):
    soma = 1
    for i in range(num, 1, -1):
        if show == 1:
            print(soma)
        soma *= i
    print(soma)


#main
while True:
    fatorial(
        int(input("Digite um número:")),
        int(input("1 ou 0 ?"))
    )
