# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def somapar(* n):
    soma = 0
    for i in n[0]:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos números pares é {soma}.')


def sorteia(x, y):
    a = randint(x, y)
    b = randint(x, y)
    c = randint(x, y)
    d = randint(x, y)
    e = randint(x, y)
    lista = [a, b, c, d, e]
    lista.sort()
    sleep(0.5)
    print(f'Sorteando...')
    sleep(2)
    print(f'Os números sorteados foram {lista}.')
    sleep(2)
    somapar(lista)


print()
print('-'*20, f'{"Sorteio":^25}', '-'*20)
inicio = int(input('Vou sortear 5 números, qual o número ínicial de referência? --> '))
fim = int(input('Qual o número final de referência? --> '))
sorteia(inicio, fim)
