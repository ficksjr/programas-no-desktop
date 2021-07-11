# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from Exercícios.desafiosfinais.desafio107 import moeda

pr = float(input('Digite um preço: '))
ma = float(input(f'De quantos % será o aumento de {pr}? -> '))
me = float(input(f'De quantos % será a redução de {pr}? -> '))

print(f'O valor digitado foi {pr}')
print(f'O valor {pr} aumentado em {ma}% é {moeda.aumentar(pr, ma)}')
print(f'O valor {pr} aumentado em {me}% é {moeda.diminuir(pr, me)}')
print(f'O dobro de {pr} é {moeda.dobro(pr)}')
print(f'A metade de {pr} é {moeda.metade(pr)}')
