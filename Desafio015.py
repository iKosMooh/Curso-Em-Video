dias = int(input('Por quantos dias ele foi alugado: '))
km = float(input('Quantos Km ele percorreu: '))

total = (dias * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))

# Check
