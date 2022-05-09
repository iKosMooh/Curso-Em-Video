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

nota1 = float(input(f'{cor["amarelo"]}Digite a primeira nota: '))
nota2 = float(input(f'{cor["amarelo"]}Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'\n{cor["vermelho"]}Sua nota é {media:.1f}, você está reprovado!')

elif media > 5 < media < 6.9:
    print(f'\n{cor["vermelho"]}Sua nota é {media:.1f}, você está de recuperação.')

elif media >= 7:
    print(f'\n{cor["verde"]}Sua nota é {media:.1f}, você foi aprovado')

# Check
