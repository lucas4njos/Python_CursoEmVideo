#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura (em cm): '))

imc = peso / (altura/100)**2

print(f'Seu IMC é de {imc:.2f}.')

if imc < 18.5:
    print('ABAIXO DO PESO!')
if 18.5 <= imc < 25:
    print('PESO IDEAL!')
if 25 <= imc < 30:
    print('SOBREPESO!')
if 30 <= imc < 40:
    print('OBESIDADE!')
if imc >= 40:
    print('OBESIDADE MÓRBIDA!')



