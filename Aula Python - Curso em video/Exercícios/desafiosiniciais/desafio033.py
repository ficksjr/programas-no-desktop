# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

import math

n1 = int(input('Diga um número: '))
n2 = int(input('Diga um segundo número: '))
n3 = int(input('Diga um terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O número {} é o maior dos três '.format(n1))
if n2 > n1 and n2 > n3:
    print('O número {} é o maior dos três '.format(n2))
if n3 > n1 and n3 > n2:
    print('O número {} é o maior dos três '.format(n3))
if n1 < n2 and n1 < n3:
    print('O número {} é o menor dos três '.format(n1))
if n2 < n1 and n2 < n3:
    print('O número {} é o menor dos três '.format(n2))
if n3 < n1 and n3 < n2:
    print('O número {} é o menor dos três '.format(n3))
