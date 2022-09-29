# Exercício Python 053: crie um programa que leia uma frase
# qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase! ")).strip().lower()
frase = frase.replace(" ", "")
inverso = ""

for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]

if frase == inverso:
    print("A Frase é um palindromo!")
else:
    print("A Frase não é um palindromo! ")
