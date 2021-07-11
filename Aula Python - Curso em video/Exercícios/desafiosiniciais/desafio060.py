# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('número:'))
numex = num
mult = 2
acumulador = 1
while num > 1:
    mult = num
    acumulador = acumulador * mult
    num -= 1

print('O fatorial de {} é {}.'.format(numex, acumulador))
