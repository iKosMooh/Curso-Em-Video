maior = 0
menor = 0

for pess in range(1, 6):
    peso = float(input('Digite o peso de uma pessoa: '))

    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso é {maior:.1f}Kg e o menor peso é {menor:.1f}Kg')
