frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece {} veses'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez em {}'.format(frase.find('A')+1))
print('A letra "A"aparece pela ultima vez em {}'.format(frase.rfind('A')))

# frase.find('A')+1 é para remover o 0 do indice iniciando por 1
