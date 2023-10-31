#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols.')

while True:
    nome = str(input('Digite o nome:'))
    gols = str(input('Digite qtd de gols:'))

    if gols.isnumeric():
        gols = int(gols)
    if gols == '':
        gols = 0

    if nome.strip() == '':
        ficha(gols=gols)
    else:
        ficha(nome, gols)
