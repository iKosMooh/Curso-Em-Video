from time import sleep

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

for c in range(10, -1, -1):
    print(f'{cor["vermelho"]}Faltam {c} segundos para estourar os fogos')
    sleep(1)
print(f'\n🎆🎆🎆🎆🎆🎆🎆🎆🎆')

# Check
