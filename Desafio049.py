num1 = int(input('Digite o número que deseja na tabuada: '))
num2 = int(input('Digite até qual número irá a a tabuada: '))

aux = 1

print('*' * 30)
print('\nTabuada:\n')
for t in range(1, num2+1):
    print(f'{aux} X {num1} = {num1 * aux}')
    aux += 1
print('*' * 30)
