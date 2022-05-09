pas = float(input('Digite quantos Km terá a sua viagem: '))

if pas <= 200:
    print('Viagem para um local com uma distância menor que 200km, R$0,50 por Km')
    print('O valor da sua viagem será: R${:.2f}'.format(pas * 0.5))
else:
    print('Viagem para um local com uma distância maior que 200km, R$0,45 por Km')
    print('O valor da sua viagem será: R${:.2f}'.format(pas * 0.45))

# Check
