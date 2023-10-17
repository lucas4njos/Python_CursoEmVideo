#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
current_year = datetime.utcnow().year

pessoa = {
            'Nome': str(input('Nome: ')),
            'Ano': int(input('Ano de nascimento: ')),
            'CTPS': int(input('CTPS: '))
        }

pessoa['Idade'] = current_year - pessoa['Ano']

if pessoa['CTPS'] != 0:
    pessoa['AnoContrato'] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salário: '))
    tempo_contrato = current_year - pessoa['AnoContrato']
    if pessoa['Idade'] + tempo_contrato < 65:
        pessoa['AnoAposentadoria'] = 65
    else:
        pessoa['AnoAposentadoria'] = pessoa['Idade'] + tempo_contrato
print('-=' * 30)
for k, v in pessoa.items():
    print(f'- {k} = {v}')
