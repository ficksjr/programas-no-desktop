# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

c1 = float(input('informe o cateto 1: '))
c2 = float(input('informe o cateto 2: '))
h1 = math.sqrt(c1*c1 + c2*c2)
print('O cateto 1 é {}, o cateto 2 é {}, a hipotenusa do triângulo retângulo equivalente é: {}.'.format(c1, c2, h1))
