# Dicionário de cores
cor = {'branco':'\033[m',
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

num1 = int(input(f'{cor["azul"]}Digite o primeiro valor: '))
num2 = int(input(f'{cor["azul"]}Digite o segundo valor: '))

if num1 > num2:
    print(f'\n{cor["cyan"]}O número {num1} do primeiro valor é o maior número.')
elif num2 > num1:
    print(f'\n{cor["cyan"]}O número {num2} do segundo valor é o maior número.')
elif num1 == num2:
    print(f'\n{cor["vermelho"]}Não existe número maior..')

# Check
