#Exercício Python 051: Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = float(input('Informe o 1° termo da PA:  '))
razao = int(input('Informe a razão da PA: '))
print(f'{termo:.0f}', end=' -> ')
for c in range(1,10):
      termo += razao
      print(f'{termo:.0f}',end=' -> ')
print('ACABOU')
