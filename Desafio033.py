num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

maior = num1
menor = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print(f'O menor número é {menor} e o maior é {maior}')

# Check
