# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.

n = str(input('Qual é o seu nome completo? ')).strip().split()

print('O seu primeiro e último nomes são é: {} {}'.format(n[0], n[len(n)-1]))
