# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

clas = ('', 'flamengo', 'inter', 'atl-mg', 'sp', 'flu', 'grêmio',
        'plameiras', 'santos', 'atl-pr', 'bragantino', 'ceará',
        'corinthians', 'atl-go', 'bahia', 'sport', 'fortaleza',
        'vasco', 'goiás', 'coritiba', 'botafogo')

print(f'Os cinco primeiros do brasileirão 2020 foram {clas[1:6]}')
print(f'Os quatro rebaixados do brasileirão 2020 foram {clas[-4:]}')
print(f'Os clubes em ordem alfabética fica: {sorted(clas)[1:]}')
print(f'A posição do bragantino é: {clas.index("bragantino")}º.')
