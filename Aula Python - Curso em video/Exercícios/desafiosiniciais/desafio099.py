# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* n):
    mai = 0
    for i in n[0]:
        if i > mai:
            mai = i
    print(f'O maior número da lista {n[0]} é {mai}.')


lista = []
while True:
    dig = (int(input('Digite um número ["999" para encerrar]: ')))
    if dig == 999:
        break
    else:
        lista.append(dig)

maior(lista)
