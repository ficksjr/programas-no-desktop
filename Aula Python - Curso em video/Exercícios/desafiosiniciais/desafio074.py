# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randrange

num = (randrange(1, 100), randrange(1, 100), randrange(1, 100), randrange(1, 100), randrange(1, 100))
print('-'*30)
print(f'Os 5 números aleatórios são os seguintes: {num}.')
print('-'*30)
print(f'O maior valor da sequência foi de {max(num)}')
print('-'*30)
print(f'O menor valor da sequência foi de {min(num)}')
print('-'*30)
