# Exercício Python 029: Escreva um programa que leia a
# velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Velocidade: '))

if velocidade > 80:
    print(f'Você foi multado em R$ {7*(velocidade-80):.2f}')
else:
    print('Tudo certo! Prossiga.')
