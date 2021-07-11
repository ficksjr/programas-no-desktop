# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random

print('Vamos jogar JOKENPO?')

player = int(input('\n [ 1 ] para pedra; \n [ 2 ] para papel; \n [ 3 ] para tesoura\nDigite aqui:'))

robo = random.randint(1, 3)

if player == robo:
    print('Você escolheu {} e eu escolhi {}. O jogo empatou'.format(player, robo))
elif player == 1 and robo == 2:
    print('Você escolheu pedra e eu escolhi papel. Você perdeu!')
elif player == 2 and robo == 1:
    print('Você escolheu papel e eu escolhi pedra. Você ganhou!')
elif player == 3 and robo == 1:
    print('Você escolheu tesoura e eu escolhi pedra. Você perdeu!')
elif player == 1 and robo == 3:
    print('Você escolheu pedra e eu escolhi tesoura. Você ganhou!')
elif player == 3 and robo == 2:
    print('Você escolheu tesoura e eu escolhi papel. Você ganhou!')
elif player == 2 and robo == 3:
    print('Você escolheu papel e eu escolhi tesoura. Você perdeu!')
