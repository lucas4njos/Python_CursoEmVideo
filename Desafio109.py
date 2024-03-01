#Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from ex109 import uteis

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
    print(f'\n{uteis.moeda(valor, show=False)}\n')
    uteis.linha()