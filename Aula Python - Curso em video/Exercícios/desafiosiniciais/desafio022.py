# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao total (sem considerar espaços).
#
# – Quantas letras tem o primeiro nome.

nome = input('Qual é o seu nome completo? ')

print('Seu nome todo em maiúsculo fica:\n{}'.format(nome.upper()))
print('Seu nome todo em minúsculo fica:\n{}'.format(nome.lower()))
print('Seu nome completo tem: \n{} letras'.format(len(nome.replace(" ", ""))))
print('Seu primeiro nome tem: \n{} letras'.format(len(nome.split()[0])))
