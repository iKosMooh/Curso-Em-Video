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

total = 0
soma = 0

for i in range(0, 500, 3):
    if i % 2:
        total += 1
        soma += i
print(f'Foram somados {total} números, e o resultado foi {soma}')

# Check
