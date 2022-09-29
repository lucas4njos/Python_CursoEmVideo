#Exercício Python 056: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
oldestman = ''
oldestman_int = 0
womenunder20 = 0

for c in range(0, 4):
    print('-'*20, f'{c+1}ª pessoa', '-'*20)
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    sex = str(input('Sexo: ')).upper().strip()

    if age > oldestman_int and sex in 'M':
        oldestman_int = age
        oldestman = name

    if age < 20 and sex in 'F':
        womenunder20 += 1

    media += age

print(f'\nMédia de idade: {media/4}')
print(f'Homem mais velho: {oldestman}')
print(f'Mulheres abaixo de 20 anos: {womenunder20}')


