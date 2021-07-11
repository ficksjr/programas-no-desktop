# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

import random
import time

c1 = int(random.randint(39, 129))

print('\nVelocidade máxima permitida na via: 80km/h. Infração grave sujeito a multa.')

print('\nDetectando a velocidade do carro 1...')

time.sleep(2)

if c1 > 80:
    print('\nO carro 1 está a {} km/h, portanto, a multa aplicada é de R${:.02f}'.format(c1, (c1-80)*7))
else:
    print('\nO carro 1 está a {} km/h, portanto, dentro do limite de velocidade'.format(c1))
