#Exercício Python 108: inclua no desafio107 uma funcao moeda, que formate para 2 casas decimais

from ex107 import uteis

valor = float(input('Digite um valor: '))

while True:

    opcao = int(input('\n1 - Aumentar\n2 - Diminuir\n3 - Dobrar\n4 - Metade\n\n'))

    if opcao == 1:
        valor = uteis.aumentar(valor)
    elif opcao == 2:
        valor = uteis.diminuir(valor)
    elif opcao == 3:
        valor = uteis.dobro(valor)
    elif opcao == 4:
        valor = uteis.metade(valor)

    uteis.linha()
    print(f'\n{uteis.moeda(valor)}\n')
    uteis.linha()