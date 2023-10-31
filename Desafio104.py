#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def leiaInt(txt):

    n = str(input(txt))
    if n.isnumeric():
        print(f'{n} é numérico.')
        return n
    else:
        print('\033[0;31mErro!\033[m')
        return ''

while True:

    n = leiaInt('Digite um número:')

    print(f'\nVariável "n" salvo com o valor: {n} \n')
