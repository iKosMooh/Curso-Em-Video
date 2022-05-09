msg = input('Digite algo: ')

print('O tipo primitivo deste valor é: {}'.format(type(msg)))
print('Só tem espaços? {}'.format(msg.isspace()))
print('É um número? {}'.format(msg.isnumeric()))
print('É alfabético? {}'.format(msg.isalpha()))
print('É alfanumérico? {}'.format(msg.isalnum()))
print('Está em maiúsculas? {}'.format(msg.isupper()))
print('Está em minúscula? {}'.format(msg.islower()))
print('Está capitalizada? {}'.format(msg.istitle()))

# Check
