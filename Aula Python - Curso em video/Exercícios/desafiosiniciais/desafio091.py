# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
# resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.

from random import randint
from operator import itemgetter

composicao = {}
for jogada in range(1, 5):
    composicao[f'jogador {jogada}'] = randint(1, 20)
for k, v in composicao.items():
    print(f'O {k} tirou {v}.')

ranking = sorted(composicao.items(), key=itemgetter(1), reverse=True)
print(type(ranking))
print(f'O ranking ficou assim: ')
cont = 1
for i in ranking:
    print(f'Em {cont}º: O {i[0]} que tirou {i[1]}.')
    cont +=1