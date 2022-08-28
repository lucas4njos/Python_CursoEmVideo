# Exercício Python 049: refaça o DESAFIO 009, mostrando a tabuada
# de um número que o usuário escolher, mas agora utilizando um laço for.

num = int(input('Deseja uma tabuada de qual número? -> '))
for i in range(0, 10):
    print(f'{num} * {i + 1} = {num * (i + 1)}')
