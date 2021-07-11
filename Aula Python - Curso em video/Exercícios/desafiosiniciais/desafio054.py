# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores.

from time import sleep

print('Informe o ano de nascimento de sete pessoas, no formato xxxx, a seguir.')
d1 = int(input('Informe o ano de nascimento da primeira pessoa: '))
d2 = int(input('Informe o ano de nascimento da segunda pessoa: '))
d3 = int(input('Informe o ano de nascimento da terceira pessoa: '))
d4 = int(input('Informe o ano de nascimento da quarta pessoa: '))
d5 = int(input('Informe o ano de nascimento da quinta pessoa: '))
d6 = int(input('Informe o ano de nascimento da sexta pessoa: '))
d7 = int(input('Informe o ano de nascimento da sétima pessoa: '))

lista = [d1, d2, d3, d4, d5, d6, d7]

print(lista)

sleep(1)
print('OK espere um segundo...')
sleep(1)

cont_maior = 0
cont_menor = 0

for i in range(0, 7):
    if 2021 - lista[i] < 18:
        print('A pessoa que nasceu em {} tem {} anos e é menor de idade'.format(lista[i], 2021 - lista[i]))
        cont_menor += 1
    else:
        print('A pessoa que nasceu em {} tem {} anos e é maior de idade'.format(lista[i], 2021 - lista[i]))
        cont_maior += 1
sleep(1)
print('OK espere mais um segundo...')
sleep(1)

print('São {} pessoas maior(es) de idade e {} menor(es) de idade'.format(cont_maior, cont_menor))
