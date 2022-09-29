#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = str(input('Digite o sexo: ')).upper().strip()[0]
    if sexo not in 'MF':
        print('Opção inválida. Tente novamente!')
    else:
        print('Parabéns, você digitou corretamente.')
        break
