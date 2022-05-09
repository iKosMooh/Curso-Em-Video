nome: str = 'a'
idade = 0
sexo: str = 'a'
media = 0
f20 = 0
maioridadeh = 0
maisvelho = nome

for pess in range(1, 5):
    print('=' * 10, f'{pess}º Pessoa', '=' * 10)
    nome = str(input('\nDigite um nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo F/M: ')).lower()
    media = media + idade

    if pess == 1:
        idade = idade
        maioridadeh = maioridadeh
    if sexo == 'f' and idade < 20:
        f20 += 1
    if sexo == 'm' and idade > maioridadeh:
        maioridadeh = idade
        maisvelho = nome

print(f'\nA média de idade do grupo é: {media / 4}')
print(f'O nome do homem mais velho é {maisvelho} com {maioridadeh} anos')
print(f'Mulheres com menos de 20 são: {f20}')


