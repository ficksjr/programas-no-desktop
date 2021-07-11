# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
saque = int(input('Quanto quer sacar? '))
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
while True:
    if saque >= 50:
        saque -= 50
        nota50 += 1
    elif 20 <= saque < 50:
        saque -= 20
        nota20 += 1
    elif 10 <= saque < 20:
        saque -= 10
        nota10 += 1
    elif 1 <= saque < 10:
        saque -= 1
        nota1 += 1
    elif saque == 0:
        break
print(f'Serão entregues {nota50} notas de R$50,00', end=', ')
print(f'{nota20} notas de R$20,00', end=', ')
print(f'{nota10} notas de R$10,00', end=' e ')
print(f'{nota1} notas de R$1,00.', end='')

