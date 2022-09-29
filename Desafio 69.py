#Exercício Python 070: Crie um programa que leia o nome e
# o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = acimademil = a = menor = 0
maisbarato = ''
while True:
    produto = str(input('Produto: '))
    price = float(input('Preço: '))

    if a < 1:
        a += 1
        menor = price
        maisbarato = produto
    if menor > price:
        menor = price
        maisbarato = produto

    total += price
    if price > 1000:
        acimademil += 1

    continua = str(input('Deseja continuar? [S] ou [N]:')).upper().strip()[0]
    if continua == 'N':
        print('Programa encerrado.')
        break
print(f"""Total gasto na compra : R$ {total:.2f}
        \nProdutos acima de R$ 1000,00 : {acimademil}
        \nProduto mais barato: {maisbarato}""")

