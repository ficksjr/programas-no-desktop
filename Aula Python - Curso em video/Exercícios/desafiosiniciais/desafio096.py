# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area(lar, comp):
    a = lar*comp
    print('-'*60)
    print(f'A largura (L) tem {lar} m, o comprimento (C) {comp} m.')
    print(f'A área (A) formada pelas medidas possui {a:.02f} m².')
    print('-' * 60)


print('-'*20, f'{"Cálculo de área":^20}', '-'*20)
largura = float(input('A largura (L) do terreno mede (em metros): '))
print('-'*60)
comprimento = float(input('A comprimento (C) do terreno mede (em metros): '))
area(largura, comprimento)
