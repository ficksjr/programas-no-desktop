# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
# não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    """
    -> Função para calcular fatorial de um número (n).
    :parâmetro n: número para se calcular o fatorial.
    :parâmetro show: (opcional) se deseja apresentar os fatores do cálculo.
    :return. O valor do fatorial do número (n) calculado.
    """
    cont = 1
    for i in range(n, 0, -1):
        if show:
            if i >= 1:
                print(f'{i}', end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        cont *= i
    return cont


help(fatorial)
# programa principal
x = int(input('Qual o número fatorial que deseja calcular? ->: '))
print(fatorial(x))
