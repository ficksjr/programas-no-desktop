# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
from math import (sin, cos, tan, radians)

a1 = radians(float(input('informe um ângulo, em graus: ')))

print('O seu seno é {:.02f}, o seu cosseno é {:.02f} e a tangente é {:.02f}.'.format(sin(a1), cos(a1), tan(a1)))
