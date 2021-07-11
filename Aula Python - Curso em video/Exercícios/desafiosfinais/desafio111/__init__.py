from Exercícios.desafiosfinais.desafio111 import moeda
from Exercícios.desafiosfinais.desafio111 import dado

pr = float(input('Digite um preço: R$ '))
ma = float(input(f'De quantos % será o aumento de {moeda.moeda(pr)}? -> '))
me = float(input(f'De quantos % será a redução de {moeda.moeda(pr)}? -> '))

moeda.resumo(pr, ma, me)