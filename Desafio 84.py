#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

pessoas = []
lista_pessoas = []

print(f'Qtd de pessoas: {len(lista_pessoas)}')
print(f'Pessoas mais pesadas: {lista_pessoas.sort(reverse= False, key= "Peso")}')


while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    lista_pessoas.append(pessoas[:])
    pessoas.clear()

    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break

print(f'Qtd de pessoas: {len(lista_pessoas)}')
print(f'Pessoas mais pesadas: {lista_pessoas.sort(key = "Peso")}')
