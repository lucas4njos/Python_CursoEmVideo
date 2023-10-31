# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
# de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.

def voto(ano):
    """
    Função para calcular idade e informar se pode ou não votar.

    :param ano: ano de nascimento
    :return: retorna uma string informando se pode ou nao votar

    Função criada por Lucas Anjos 27/10/2023
    github: lucas4njos
    """
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        return ('NEGADO')
    elif idade >= 18:
        return ('OBRIGATÓRIO')
    else:
        return ('OPCIONAL')


# main

while True:
    print(voto(int(input("Por favor, digite seu ano de nascimento: "))))
