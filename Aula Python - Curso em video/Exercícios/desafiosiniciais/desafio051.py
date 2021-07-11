# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

A1 = int(input('Informe o Primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
print('Segue os 10 primeiros termos dessa PA: ')
for i in range(A1, A1+10*r, r):
    print(i)
