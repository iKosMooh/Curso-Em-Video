r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))

triangulo: str = 'NÃO FORMOU'

if r1 + r2 < r3 and r2 + r3 < r1 and r1 + r3 < r2:
    triangulo = 'FORMOU'
else:
    print(f'Você {triangulo} um triângulo')
