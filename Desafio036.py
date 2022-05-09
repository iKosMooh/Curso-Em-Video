print('\n\033[33mVocê deseja realizar um empréstimo para comprar uma casa, '
      'então responda as perguntas a baixo para saber se o aprovaremos ou não.\n')

casa = float(input('\033[33mQual é o valor da casa que irá comprar: '))
sal = float(input('\033[33mQual é o seu salário: '))
data = int(input('\033[33mVocê pagará em quantos anos: '))

meses = data * 12
prestacao = casa / meses

if prestacao >= sal * 0.3:
    print('\n\033[31mSeu empréstimo foi negado, as prestações são superiores a 30% de seu salário!')
    print(f'\nValor da casa: R${casa}')
    print(f'Valor do salário: R${sal}')
    print(f'Pagaria em quantos anos: {data}')
    print(f'Valor das prestações: R${prestacao:.2f}')
else:
    print('\n\033[32mSeu empréstimo foi aprovado, você cumpre os requisitos!')
    print(f'\033[32mVocê pagará R${prestacao:.2f} por mês durante {data} ano/s SEM JUROS')
    print(f'\nValor da casa: R${casa}')
    print(f'Valor do salário: R${sal}')
    print(f'Pagaria em quantos anos: {data}')
    print(f'Valor das prestações: R${prestacao:.2f}')

# Check
