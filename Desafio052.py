num = int(input('Digite um número: '))

if num > 1:
    for i in range(2, num):
        if (num % 2) == 0:
            print(f'\n{num} não é um número primo')
            break
    else:
        print(f'\n{num} é Número primo')
