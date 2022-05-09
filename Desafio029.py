vel = int(input('Digite a velocidade do carro: '))
multa: float = (vel - 80) * 7

if vel >= 80:
    print('A velocidade permitida da pista era 80Km')
    print('Você passou pelo radar à {}kmh e foi multado em R${:.2f}'.format(vel, multa))

print('\nVelociade dentro do pertimitdo!')

# Check
