# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número para verificar se ele é primo ou não: '))

cont = 0

for i in range(2, num):
    print(i)
    if num % i == 0:
        cont = cont + 1
        print('O número {} é multiplo de {}'.format(num, i))
    if cont >= 1:
        break

if cont >= 1:
    print('O número {} não é primo'.format(num))
else:
    print('O número {} é primo'.format(num))
