# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

n = str(input('Qual é seu nome completo? ')).strip()

print('O seu nome possui o nome Silva? {}'.format('silva' in n.lower().split()))
