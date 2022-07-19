# Exercício Python 039: faça um programa que leia o ano de nascimento de um jovem
# e informe, conforme a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year

ano = int(input('Digite o seu ano de nascimento: '))

idade = ano_atual - ano

if idade < 18:
    print(f'Você ainda não precisa se alistar. Mas atente-se: faltam {(idade-18)*-1} anos.')
elif idade > 18:
    print(f'Você já deveria ter se alistado!. Isso foi há {idade-18} ano(s).')
elif idade == 18:
    print('Pois é amigão, chegou a hora.')
