#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

stats = dict()

stats['Nome'] = str(input('Digite o nome do jogador: '))
stats['Qtd_Partidas'] = int(input('Quantas partidas?'))

total_gols = 0

for i in range(0, stats['Qtd_Partidas']):
    stats[f'Partida_{i+1}'] = int(input(f'Quantos gols na partida {i+1}?'))
    total_gols += stats[f'Partida_{i+1}']

stats['Total_De_Gols'] = total_gols

for k, v in stats.items():
    print(f'{k}: {v}')
