# Dicionário de cores
cor = {'branco': '\033[m',
       'amarelo': '\033[33m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'azul': '\033[34m',
       'roxo': '\033[35m',
       'cyan': '\033[36m',
       'cinza': '\033[37m',
       'b': '\033[1:m',
       'under': '\033[4:m',
       'reverse': '\033[7:m'}

r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))

triangulo: str = 'NÃO FORMOU'

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    triangulo = 'FORMOU'
    print(f'{cor["verde"]}')

else:
    print(f'\n{cor["vermelho"]}Você {triangulo} um triângulo')

if r1 == r2 == r3 and triangulo == 'FORMOU':
    print(f'Você {triangulo} um triângulo Equilátero')

elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1 and triangulo == 'FORMOU':
    print(f'Você {triangulo} um triângulo Isóceles')

elif r1 != r2 != r3 != r1 and triangulo == 'FORMOU':
    print(f'Você {triangulo} um triângulo Escaleno')

# Check
