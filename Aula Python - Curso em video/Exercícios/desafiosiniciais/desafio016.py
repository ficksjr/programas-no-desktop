# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
# Inteira.

import math

n = float(input('Digíte um número que seja "quebrado": '))
n1 = math.trunc(n)
print('O número inteiro fica {}'.format(n1))
