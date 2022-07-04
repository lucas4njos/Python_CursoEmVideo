#Exercício Python 25: Crie um programa que leia o nome de
# uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite um nome: ')).upper().strip()

if "SILVA" in nome:
    print('Este nome possui "SILVA".')
else:
    print('Este nome não possui "SILVA"')