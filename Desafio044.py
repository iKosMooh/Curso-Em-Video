# Dicionário de cores
cor = {'branco': '\033[m',
       'amarelo': '\033[33m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'azul': '\033[34m',
       'roxo': '\033[35m',
       'cyan': '\033[36m',
       'cinza': '\033[37m',
       'b': '\033[1:m',
       'under': '\033[4:m',
       'reverse': '\033[7:m'}

valor = float(input(f'{cor["verde"]}Valor do produto a ser pago: R$'))

print(f'{cor["azul"]}Selecione o modo de pagamento:')

print('{}1 {}Á vista no {}cheque ou dinheiro {}10% {}de desconto'
      .format(cor["amarelo"], cor["branco"], cor["verde"], cor["amarelo"], cor["branco"]))

print('{}2 {}Á vista no {}cartão {}5% {}de desconto'
      .format(cor["amarelo"], cor["branco"], cor["verde"], cor["amarelo"], cor["branco"]))

print('{}3 {}2x no {}cartão {}preço normal'
      .format(cor["amarelo"], cor["branco"], cor["verde"], cor["branco"]))

print('{}4 {}3x ou mais {}no cartão {}20% {}de juros'
      .format(cor["amarelo"], cor["branco"], cor["verde"], cor["amarelo"], cor["branco"]))

op = int(input('\n  Modo selecionado: '))

if op == 1:
    valor = valor * 0.9
    print('\n{}Você escolheu: {}1 {}Á vista no {}cheque ou dinheiro {}10% {}de desconto'
          .format(cor["verde"], cor["amarelo"], cor["branco"], cor["verde"], cor["amarelo"], cor["branco"]))
    print(f'\nO valor a ser pago será: {cor["verde"]}R${valor:.2f}')

elif op == 2:
    valor = valor * 0.95
    print('\n{}Você escolheu: {}2 {}Á vista no {}cartão {}5% {}de desconto'
          .format(cor["verde"], cor["amarelo"], cor["branco"], cor["verde"], cor["amarelo"], cor["branco"]))
    print(f'\nO valor a ser pago será: {cor["verde"]}R${valor:.2f}')

elif op == 3:
    print('\n{}Você escolheu: {}3 {}2x no {}cartão {}preço normal'
          .format(cor["verde"], cor["amarelo"], cor["branco"], cor["verde"], cor["branco"]))
    print(f'\nO valor a ser pago será: {cor["verde"]}R${valor:.2f}')

elif op == 4:
    valor = valor * 1.2
    parcela = int(input('\n  Quantas parcelas: '))
    parcelado = valor / parcela
    print('\n{}Você escolheu: {}4 {}3x ou mais {}no cartão {}20% {}de juros'
          .format(cor["verde"], cor["amarelo"], cor["branco"], cor["verde"], cor["amarelo"], cor["branco"]))
    print(f'\nO valor total COM JUROS a ser pago será de {cor["verde"]}R${valor:.2f}{cor["branco"]} '
          f'parcelado em {parcela}x')
    print(f'{cor["branco"]}O valor a ser pago mensal será de {cor["verde"]}R${parcelado:.2f}')
else:
    print(f'{cor["vermelho"]}\nEsta opção não existe!')
