#Exercício Python 27: Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o nome completo de uma pessoa: ')).strip().split()

primeiro = nome[0]
ultimo = nome[len(nome)-1]

print(f'Seu primeiro nome é {primeiro}.')
print(f'Seu último nome é {ultimo}.')