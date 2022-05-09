sal = float(input('Digite o seu salário: '))

aumento = sal

if sal >= 1250:
    sal = sal * 1.10
    aumento = sal * 0.10
    print('Seu salário é maior que R$1250,00 então seu aumento é de 10%')
    print(f'Seu aumento é de R${aumento:.2f}')
    print(f'Seu salário com o novo aumento é R${sal:.2f}')
else:
    sal = sal * 1.15
    aumento = sal * 0.15
    print('Seu salário é menor que R$1250,00 e seu aumento foi de 15%')
    print(f'Seu aumento é de R${aumento:.2f}')
    print(f'Seu salário com seu novo aumento é R${sal:.2f}')

# Check
