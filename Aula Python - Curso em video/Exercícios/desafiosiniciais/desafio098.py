# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
# fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(i, f, r):
    print('   -->', end=' ')
    sleep(0.5)
    if r < 0:
        r *= -1
    if r == 0:
        r = 1
    if i < f:
        while i <= f:
            print(i, end=' ')
            sleep(0.1)
            i += r

    elif i >= f:
        while i >= f:
            print(i, end=' ')
            sleep(0.1)
            i -= r


print('-=' * 23)
print('Iniciando contagem de 1 até 10, de 1 em 1:')
contador(1, 10, 1)
print()
print('-=' * 23)
print('Iniciando contagem de 10 até 0, de 2 em 2:')
contador(10, 0, 2)
print()
print('-=' * 23)
print('Agora é a sua vez')
inicio = int(input('Qual é o primeiro termo da contagem? -> '))
fim = int(input('Até que número deseja contar? -> '))
passo = int(input('Qual o passo da contagem? ->'))
contador(inicio, fim, passo)
print()
print('-=' * 23)
