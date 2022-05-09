n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print()
print('A soma é {}, a produto é {}, a divisão é {:.3f},'.format(s, m, d), end=' ')
print('a divisão inteira é {} e a exponenciação é {}'.format(di, e))

# Check
