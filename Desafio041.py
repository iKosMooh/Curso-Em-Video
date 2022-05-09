from datetime import date
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

born = int(input(f'{cor["azul"]}Digite seu ano de nascimento: '))
data = date.today().year
idade = data - born

if idade <= 9:
       print(f'Você tem {idade} anos e é classificado como Mirim')
elif idade > 9 < idade <= 14:
       print(f'Você tem {idade} anos e é classificado como Infantil')
elif idade > 14 < idade <= 19:
       print(f'Você tem {idade} anos e é classificado como Junior')
elif idade > 19 < idade <= 20:
       print(f'Você tem {idade} anos e é classificado como Sênior')
elif idade > 20:
       print(f'Você tem {idade} anos e é classificado como Master')

# Check
