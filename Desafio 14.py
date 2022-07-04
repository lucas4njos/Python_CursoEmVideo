#Exercício Python 14: Escreva um programa que converta uma
# temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('*'*8,'CONVERSOR DE GRAUS CELSIUS PARA FAHRENHEIT','*'*8)

temperatura = float(input('Digite a temperatura em ºC: '))

temperatura = (temperatura * 1.8) + 32

print(f'Temperatura em ºF: {temperatura}')