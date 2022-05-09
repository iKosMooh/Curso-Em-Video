import random

a1 = str(input('Insira o nome de um aluno: '))
a2 = str(input('Insira o nome de um aluno: '))
a3 = str(input('Insira o nome de um aluno: '))
a4 = str(input('Insira o nome de um aluno: '))

lista = [a1, a2, a3, a4]

random.shuffle(lista)
print('Os alunos sorteados respectivamente foram foram: ')
print(lista)

# Check
