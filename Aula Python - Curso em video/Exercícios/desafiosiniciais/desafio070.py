# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
# o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.
print('-'*3, 'lista de produtos', '-'*3)
soma = 0
cont = 0
menor = 0
nomen = ''

while True:
    nomep = str(input('Digite o nome do produto: ')).strip().upper()
    precop = float(input('Digite o preço deste produto: '))
    soma += precop
    if precop > 1000:
        cont += 1
    if cont == 1:
        menor = precop
    if precop <= menor:
        menor = precop
        nomen = nomep
    esc = str(input('Deseja continuar adicionando dados? [S/N]: ')).strip().upper()
    if esc in 'N':
        break
print(f'O total gasto na compra é de R${soma:.02f}.')
print(f'Há {cont} produto(s) com valor maior que R$1000,00.')
print(f'O produto mais barato é o {nomen}.')
