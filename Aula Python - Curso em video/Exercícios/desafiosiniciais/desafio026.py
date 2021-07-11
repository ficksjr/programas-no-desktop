# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

n = str(input('Diga uma frase: ')).lower().strip()

print('A letra "a" aparece {} vezes na frase.'.format(n.count('a')))
print('A primeira aparece na posição {}'.format(n.find('a')+1))
print('A última aparece na posição {}'.format(n.rfind('a')+1))
