#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

alunos = dict()
qtd_notas = 0
maior_nota = 0
menor_nota = 0
media_turma = 0
situacao = ''

def notas(tpl, verSituacao = False):

    soma = 0

    for i in range(0, len(tpl)):
        if i == 0:
            maior_nota = menor_nota = tpl[i]

        if i > maior_nota:
            maior_nota = i
        elif i < menor_nota:
            menor_nota = i

        soma += i

        media_turma = soma / len(tpl)

    alunos['Qtd_Notas'] = len(tpl)
    alunos['Maior_Nota'] = maior_nota
    alunos['Menor_Nota'] = menor_nota
    alunos['Media_Turma'] = media_turma

    if verSituacao:
        situacao = 'Ruim'
        alunos['Situacao'] = situacao

    print(alunos)


notas((5, 25, 10, 3, 4, 115, 9, 2), verSituacao=False)


