#Exercício Python 089: Crie um programa que leia nome e
# duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.

notas = []
lista_final = []

qtd_alunos = int(input('Quantos alunos deseja cadastrar? '))

for c in range(0, qtd_alunos):
    notas.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1:')))
    notas.append(float(input('Nota 2:')))

    lista_final.append(notas[:])
    notas.clear()

print(lista_final)

for c in range(0, qtd_alunos):
    print(lista_final[c][0], (lista_final[c][1] + lista_final[c][2])/ 2 )

consultar_aluno = int(input('Deseja conferir a nota de algum aluno? '))
print(lista_final[consultar_aluno - 1])