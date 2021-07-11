# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
# forem pares. Se o valor digitado for ímpar, desconsidere-o.

from random import randint

num = 0
soma = 0
print('Os números são os seguintes:')
for i in range(1, 7):
    num = randint(1, 100)
    print(num)
    if num % 2 == 0:
        soma = soma + num

print('A soma dos números pares entre estes 6 números é: {}'.format(soma))
