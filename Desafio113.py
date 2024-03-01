#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(str):
    try:
        num = input(str)
        return(int(num))
    except Exception as error:
        print(f'Erro: {error}')


while True:
    leiaInt('Digite um número inteiro: ')