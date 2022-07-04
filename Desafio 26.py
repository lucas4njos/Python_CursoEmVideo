#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra “A”;
# Em que posição ela aparece a primeira vez;
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

# Quantas vezes aparece a letra “A”;
r1 = frase.count('A')
print(f'A letra "A" aparece {r1} vezes.')

# Em que posição ela aparece a primeira vez;
r2 = frase.find('A')
print(f'A letra "A" aparece pela primeira vez na posição {r2+1}.')

# Em que posição ela aparece a última vez.
r3 = frase.rfind('A')
print(f'A letra "A" aparece pela última vez na posição {r3+1}.')

