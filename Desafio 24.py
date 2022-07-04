#Exercício Python 24: Crie um programa que leia o
# nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: ')).upper().strip()

if cidade[:5] == "SANTO":
    print(f'A cidade "{cidade}" começa com "SANTO".')
else:
    print(f'A cidade "{cidade}" não começa com "SANTO".')