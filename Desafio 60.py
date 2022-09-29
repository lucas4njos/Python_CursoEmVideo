#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número: '))
fat = num
i = fat-1
while True:
    fat = fat * i
    i -= 1
    if i == 1:
        break
print(f'Fatorial: {fat}')