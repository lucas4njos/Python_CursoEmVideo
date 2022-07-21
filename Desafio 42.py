#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

a = float(input('Reta A: '))
b = float(input('Reta B: '))
c = float(input('Reta C: '))


if a < (b + c) and b < (a+c) and c < (b+a):
    print('Conseguimos formar um triângulo com essas medidas')
    if a == b and b == c:
        print('Triangulo EQUILATERO')
    elif a == b or a == c or b == c:
        print('Triangulo ISOSCELES')
    elif  a != b !=c:
        print('Triangulo ESCALENO')
else:
    print('Não conseguimos fazer um triângulo com essas medidas')