from random import randint

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

print('\n{}Escolha uma das opções para jogar com o computador!\n'.format(cor["verde"]))

print('{}1{} Pedra'.format(cor["amarelo"], cor["branco"]))
print('{}2{} Papel'.format(cor["amarelo"], cor["branco"]))
print('{}3{} Tesoura'.format(cor["amarelo"], cor["branco"]))

p = int(input('\n{}Opção escolhida: '.format(cor["verde"])))

pc = randint(1, 3)

if p == pc:
    print(f'\n{cor["amarelo"]}Empate vocês escolheram o mesmo')

elif p == 2 and pc == 1:
    print(f'\n{cor["verde"]}Você venceu desta vez você escolheu Papel e ele escolheu Pedra')

elif pc == 2 and p == 1:
    print(f'\n{cor["vermelho"]}Não foi desta vez HaHaHa, você escolheu Pedra e ele escolheu Papel')

elif p == 3 and pc == 2:
    print(f'\n{cor["verde"]}Você venceu desta vez você escolheu Tesoura e ele escolheu Papel')

elif pc == 3 and p == 2:
    print(f'\n{cor["vermelho"]}Não foi desta vez HaHaHa, você escolheu Papel e ele escolheu Tesoura')

elif p == 1 and pc == 3:
    print(f'\n{cor["verde"]}Você venceu desta vez você escolheu Pedra e ele escolheu Tesoura')

elif pc == 1 and p == 3:
    print(f'\n{cor["vermelho"]}Não foi desta vez HaHaHa, você escolheu Tesoura e ele escolheu Pedra')

else:
    print(f'\n{cor["vermelho"]}Opção selecionada invalida')

# Check
