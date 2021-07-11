# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se
# o usuário venceu ou perdeu.

import random

n = random.randint(0, 5)
m = int(input('Jogo da advinhação: Advinhe qual o número escolhi entre 0 e 5: '))
if m == n:
    print('Você acertou!')
else:
    print('Você errou! O número era {}.'.format(n))
