from random import randint

num = randint(0, 5)

r = int(input('Digite o número que você acha que caiu: '))

if num == r:
    print('*' * 23, '\nVocê acertou! Parabéns!\n', '*' * 22)
else:
    print('*' * 42, '\nVocê errou tente novamente o número era {}\n'.format(num), '*' * 41)

# Check
