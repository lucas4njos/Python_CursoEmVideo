#Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

alunos = {}

alunos['nome'] = str(input("Digite um nome: "))
alunos['media'] = float(input("Digite a média: "))

print(alunos)

