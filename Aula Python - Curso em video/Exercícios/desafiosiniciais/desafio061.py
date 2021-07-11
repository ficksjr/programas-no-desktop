# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.

pt = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão da PA: '))

numtermos = 0
print('Os 10 primeiros termos desta PA são:')
while numtermos < 10:
    print('{}'.format(pt + numtermos * ra), end='')
    print(', ' if numtermos < 9 else '.', end='')
    numtermos += 1
