#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = maior = menor = quantidade = soma = loop = 0
menor = 15**56
while True:
    while loop == 0:
        num = int(input('Digite um número: '))
        continua = str(input('Deseja continuar? Digite SIM ou NÃO:')).upper().strip()[0]
        quantidade += 1
        soma += num
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        if continua == 'N':
            loop = 1
    media = soma / quantidade
    print(f'\nMedia: {media} | Maior: {maior} | Menor: {menor}')
    continua = str(input('Deseja continuar? Digite SIM ou NÃO:')).upper().strip()[0]
    if continua == 'S':
        loop = 0
    elif continua == 'N':
        break
    else:
        print('Opção inválida! Programa encerrado.')
        break

