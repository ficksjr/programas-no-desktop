# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga
# mostrar os números como um valor monetário formatado.

from Exercícios.desafiosfinais.desafio108 import moeda

pr = float(input('Digite um preço: R$ '))
ma = float(input(f'De quantos % será o aumento de {moeda.moeda(pr)}? -> '))
me = float(input(f'De quantos % será a redução de {moeda.moeda(pr)}? -> '))

print(f'O valor digitado foi {moeda.moeda(pr)}')
print(f'O valor {moeda.moeda(pr)} aumentado em {ma}% é {moeda.moeda(moeda.aumentar(pr, ma))}')
print(f'O valor {moeda.moeda(pr)} aumentado em {me}% é {moeda.moeda(moeda.diminuir(pr, me))}')
print(f'O dobro de {moeda.moeda(pr)} é {moeda.moeda(moeda.dobro(pr))}')
print(f'A metade de {moeda.moeda(pr)} é {moeda.moeda(moeda.metade(pr))}')
