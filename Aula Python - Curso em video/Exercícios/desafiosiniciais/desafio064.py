# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).

num = int(input('Advinhe um número entre 1 e 100: '))
ac = num
cont = 0
while num != 99:
    ac += num
    cont += 1
    num = int(input('Errou! Digite outro número: '))
print('Acertou! A soma dos {} números errados é: {}'.format(cont, ac))
