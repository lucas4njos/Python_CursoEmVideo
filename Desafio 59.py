#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

while True:
    menu = int(input("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Digite uma opção:  """))
    if menu == 1:
        print(f'Soma: {v1 + v2}')
    elif menu == 2:
        print(f'Multiplicação: {v1 * v2}')
    elif menu == 3:
        if v1 > v2:
            print(f'Maior número: {v1}')
        elif v1 < v2:
            print(f'Maior número: {v2}')
        else:
            print('São iguais!')
    elif menu == 4:
        print('Ok, novos números!')
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida. Tente novamente.')

