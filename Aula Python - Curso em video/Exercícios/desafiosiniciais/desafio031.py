# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

v = float(input('\nQual é a distância da viagem, em km? '))

if v > 200:
    print('\nO valor da passagem de uma viagem de {} km é: R${:.02f} '.format(v, v*0.45))
else:
    print('\nO valor da passagem de uma viagem de {} km é: R${:.02f} '.format(v, v*0.5))
