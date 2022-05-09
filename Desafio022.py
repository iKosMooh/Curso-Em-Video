nome = str(input('Digite o nome de uma pessoa: '))
primeiro = nome.split()

print('O nome em maiúsculo é: {}'.format(nome.upper()))
print('O nome em minúsculo é: {}'.format(nome.lower()))
print('O nome tem um Total de {} letras'.format(len(''.join(primeiro))))
print('O primeiro nome tem um total de {} letras'.format(len(primeiro[0])))

# Check
