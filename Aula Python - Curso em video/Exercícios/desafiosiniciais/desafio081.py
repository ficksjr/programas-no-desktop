# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

cont = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1
    esc = str(input('Deseja continuar? [S/N]: '))
    if esc in 'Nn':
        break

print(f'\n{cont} números digitados.')
print(f'A lista ficou: {sorted(lista, reverse=True)}.')
if 5 in lista:
    print('5 está na lista.')
else:
    print('5 não está na lista.')
