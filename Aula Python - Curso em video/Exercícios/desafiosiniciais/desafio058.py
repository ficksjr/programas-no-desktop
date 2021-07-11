# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num1 = input('Jogo da adivinhação: Advinhe o número que eu pensei, de 1 a 10: ').strip()
while num1 not in '12345678910':
    num1 = input('Utilize um número de 1 a 10: ')
num1 = int(num1)
if num1 not in range(1, 11):
    num1 = input('Utilize um número de 1 a 10: ')
num1 = int(num1)
numbot = randint(1, 10)
cont = 1

while num1 != numbot:
    num1 = (input('Errou! Tente de novo, um número de 1 a 10: '))
    while num1 not in '12345678910':
        num1 = input('Utilize um número de 1 a 10: ')
    num1 = int(num1)
    if num1 not in range(1, 11):
        num1 = input('Utilize um número de 1 a 10: ')
    num1 = int(num1)
    cont += 1

print('Acertou! O número que eu pensei era {}. Foram necessárias {} vez(es) para acertar'.format(numbot, cont))
