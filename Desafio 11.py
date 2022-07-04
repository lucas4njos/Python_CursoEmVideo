#Exercício Python 11: Faça um programa que leia a largura e a altura
# de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2 metros quadrados.

largura = float(input('Digite a \033[33mlargura\033[m de sua parede em metros: '))
altura = float(input('Digite a \033[33maltura\033[m de sua parede em metros:'))

print(f'A área de sua parede corresponde a \033[36m{largura * altura}\033[m metros quadrados.\n'
      f'Portanto, você irá precisar de \033[36m{(largura * altura) / 2}\033[m litros de tinta.')

