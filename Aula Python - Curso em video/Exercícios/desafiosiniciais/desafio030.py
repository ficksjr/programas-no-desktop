# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('\nEscreva um número inteiro qualquer: '))

n2 = (n % 2)

if n2 == 0:
    print('\nO número {} é par!'.format(n))
else:
    print('\nO número {} é ímpar!'.format(n))
