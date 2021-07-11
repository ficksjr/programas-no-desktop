# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci. Exemplo:

num = int(input('Digite o número de termos da sequência Fibonacci que queira que eu mostre: '))

print('A sequência de Fibonacci para {} termo(s) é:'.format(num))

i = num
num = 0
numA = 1
numB = 0
while i > 0:
    print('{}'.format(num), end=' ')
    num = numA + numB
    numA = numB
    numB = num
    i -= 1

