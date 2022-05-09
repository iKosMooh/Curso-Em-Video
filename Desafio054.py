from datetime import date

data = date.today().year

totmaior = 0
totmenor = 0

for pess in range(1, 8):
    born = int(input('Digite um ano de nascimento: '))
    idade = data - born

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'O total de pessoas que atingiram a maioridade foi {totmaior} e que não atingiram foi {totmenor}')
