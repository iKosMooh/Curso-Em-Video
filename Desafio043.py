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

peso = float(input(f'{cor["amarelo"]}Informe o seu peso: '))
altura = float(input('Informe sua altura em metros: '))

imc = peso / (altura * altura)

if imc < 18:
    print(f'\nSeu índice de massa corporal é {cor["verde"]}{imc:.1f}{cor["amarelo"]}, e você é considerado como baixo '
          f'peso')

elif imc > 18 < imc < 24:
    print(f'\nSeu índice de massa corporal é {cor["verde"]}{imc:.1f}{cor["amarelo"]}, e você é considerado normal')

elif imc > 24 < imc < 34:
    print(f'\nSeu índice de massa corporal é{cor["verde"]}{imc:.1f}{cor["amarelo"]}, e você é considerado com sobrepeso'
          )

elif imc > 35 < imc < 40:
    print(f'\nSeu índice de massa corporal é {cor["vermelho"]}{imc:.1f}{cor["amarelo"]}, e você possui obesidade '
          f'moderada')

elif imc > 40:
    print(f'\nSeu índice de massa corporal é {cor["vermelho"]}{imc:.1f}{cor["amarelo"]}, e você possui obesidade grave')

# Check
