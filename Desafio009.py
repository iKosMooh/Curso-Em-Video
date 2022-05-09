n = float(input('Digite um número para a tabuada: '))

aux = 1

print('*' * 20)
print('O número selecionado para a tabuada foi: {}'.format(n))
print('*' * 20)

while (aux <= 10):
    print('{} X {} = {}'.format(aux, n, aux * n))
    aux = aux + 1

print('*' * 20)

# Check
