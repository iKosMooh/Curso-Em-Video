# Dicionário de cores
cores = {'branco':'\033[m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'cyan':'\033[36m',
         'cinza':'\033[37m',
         'b':'\033[1:m',
         'under':'\033[4:m',
         'reverse':'\033[7:m'}

num = int(input('Digite um número para a conversão: '))


binary = bin(num)
octal = oct(num)
hexadecimal = hex(num)

print(f'\n{cores["azul"]}Escolha uma das alternativas para realizar a conversão: \n')
print('{}- {}1 {}para {}Binário'.format(cores['amarelo'], cores['azul'], cores['branco'], cores['azul']))
print('{}- {}2 {}para {}Octal'.format(cores['amarelo'], cores['azul'], cores['branco'], cores['azul']))
print('{}- {}3 {}para {}Hexadecimal'.format(cores['amarelo'], cores['azul'], cores['branco'], cores['azul']))

escolha = int(input('\n  '))

if escolha == 1:
    print('\nResultado: {}'.format(binary[2:]))
elif escolha == 2:
    print('\nResultado: {}'.format(octal[2:]))
elif escolha == 3:
    print('\nResultado: {}'.format(hexadecimal[2:]))
else:
    print('{}Escolha invalida'.format(cores['vermelho']))

# Check
