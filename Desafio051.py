t1 = int(input('Digite o termo inicial: '))
num = int(input('Digite um número para realizar a Progressão Aritmética: '))
t2 = int(input('Digite a quantidade de termos: '))
decimo = t1 + (t2 - 1) * num

for pa in range(t1, decimo + num, num):
    print(pa, end=' -> ')
print('FIM')

