#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com
# vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

stats = dict()
gols = []
elenco = []
a = True

while True:
    while a == 1:
        gols.clear()
        print('+=' * 45)

        stats['Nome'] = str(input('Digite o nome do jogador: '))
        stats['Qtd_Partidas'] = int(input('Quantas partidas?'))

        total_gols = 0

        for i in range(0, stats['Qtd_Partidas']):
            gols.append(int(input(f'Quantos gols na partida {i+1}?')))
            total_gols += gols[i]
        stats['Gols'] = gols.copy()
        stats['Total_De_Gols'] = total_gols

        elenco.append(stats.copy())

        print('+=' * 45)
        for jogador in elenco:
            print(f'{jogador}')
        print('+=' * 45)

        while True:
            continuar = str(input("Deseja continuar? [S/N]: "))
            if continuar not in 'SsNn':
                print("Digite S ou N!")
            elif continuar in 'Ss':
                break
            elif continuar in 'Nn':
                a = False
                break

    print('+=' * 45)
    ver_jogador = int(input("\nQual jogador deseja ver?"))
    print(f'\n{elenco[ver_jogador]}')
    print('+=' * 45)



