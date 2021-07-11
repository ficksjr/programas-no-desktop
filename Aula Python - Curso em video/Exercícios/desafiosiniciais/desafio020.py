# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

alunos = 'Pedro José João Lucas'.split()

print(alunos)

shuffle(alunos)

print('A nova disposição dos alunos é: {}'.format(alunos))
