import datetime
# Dicionário de cores
cor = {'branco':'\033[m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'verde':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'cyan':'\033[36m',
         'cinza':'\033[37m',
         'b':'\033[1:m',
         'under':'\033[4:m',
         'reverse':'\033[7:m'}

born = int(input(f'{cor["cyan"]}Digite seu ano de nascimento: '))

ano = datetime.date.today().year

if ano - born < 18:
    print(f'{cor["cyan"]}Você tem {ano - born} e terá que se alistar no serviço militar em '
          f'{cor["amarelo"]}{18 - (ano - born)} {cor["cyan"]} ano/s!')
    print(f'Você terá que se alistar em {cor["amarelo"]}{ano - (ano - born) + 18}')

elif ano - born > 18:
    print(f'{cor["cyan"]}Você tem {ano - born} e deveria ter se alistado hà {cor["vermelho"]}{ano - born - 18}{cor["cyan"]} ano/s atrás!')
    print(f'Você deveria se alistar em {cor["amarelo"]}{ano - (ano - born) + 18}')

elif ano - born == 18:
    print(f'{cor["amarelo"]}Está na hora de se alistar no serviço militar!')

# Check
