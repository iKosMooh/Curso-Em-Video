frase = str(input('Digite uma palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('A frase é um palíndomo')
else:
    print('\nNão é um palindromo')

# Check
