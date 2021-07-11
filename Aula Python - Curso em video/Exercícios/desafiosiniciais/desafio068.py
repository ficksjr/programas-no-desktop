# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
cont = 0
print('Vamos jogar par ou ímpar!')
while True:
    num_j = int(input('Escolha um número:'))
    esc_j = str(input('Você quer PAR ou ÍMPAR? [P/I]: ')).strip().lower()
    num_bot = randint(1, 2)
    soma = num_j + num_bot
    if esc_j in 'Pp':
        if soma % 2 == 0:
            print(f'Você escolheu {num_j} e eu escolhi {num_bot}, deu par, você escolheu par. Ganhou!')
        else:
            print(f'Você escolheu {num_j} e eu escolhi {num_bot}, deu ímpar, você escolheu par. Perdeu!!')
            break
    elif esc_j in 'IiÍí':
        if soma % 2 == 0:
            print(f'Você escolheu {num_j} e eu escolhi {num_bot}, deu par, você escolheu ímpar. Perdeu!')
            break
        else:
            print(f'Você escolheu {num_j} e eu escolhi {num_bot}, deu ímpar, você escolheu ímpar. Ganhou!!')
    cont += 1
print(f'Você ganhou {cont} vezes seguidas!')
