#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

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
    print(f'\n{valor}\n')
    uteis.linha()