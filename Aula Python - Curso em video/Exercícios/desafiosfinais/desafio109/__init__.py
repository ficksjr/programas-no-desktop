# Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a
# mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
# desafio 108.

from Exercícios.desafiosfinais.desafio109 import moeda

pr = float(input('Digite um preço: R$ '))
ma = float(input(f'De quantos % será o aumento de {moeda.moeda(pr)}? -> '))
me = float(input(f'De quantos % será a redução de {moeda.moeda(pr)}? -> '))

moeda.resumo(pr, ma, me)


