# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.

from random import sample as samp
from time import sleep

lista_mega_total = []

for num_total in range(1, 61):
    lista_mega_total.append(num_total)

vezes_jogo = int(input('Quantos jogos aleatórios da MEGA SENA deseja fazer? '))

for num_jogo in range(0, vezes_jogo):
    print(f'Jogo número {num_jogo+1} : {sorted(samp(lista_mega_total, k=6))}')
    sleep(1)
