print('*' * 30)
num = int(input('Digite um número: '))

m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print('Milhar : {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena : {}'.format(d))
print('Unidade: {}'.format(u))

print('*' * 30)

# Check
