from datetime import date

data = int(input('Digite qual ano quer analisar, ou coloque 0 para analisar o ano atual: '))

if data == 0:
    data = date.today().year
if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print(f'O Ano {data} bissexto')
else:
    print(f'O Ano {data} não é bissexto')