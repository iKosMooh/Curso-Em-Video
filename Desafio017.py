from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hi = hypot(co, ca)

print('A hipotenusa do triângulo é: {:.2f}'.format(hi))

# Check
