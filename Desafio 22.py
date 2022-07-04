#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao td sem considerar espaços
#– Quantas letras tem o primeiro nome.

nome = str(input(("Digite o nome completo de uma pessoa: ")))

print(f'--> Em maiúsculo: {nome.upper()}')
print(f'--> Em minúsculo: {nome.lower()}')
print(f'--> Quantas letras ao todo: {len(nome) - nome.count(" ")}')
print(f'--> Quantas letras tem o primeiro nome: {nome.find(" ")}')
