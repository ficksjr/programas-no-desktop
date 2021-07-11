# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

num1 = 1
soma = 0
cont = 0
while num1 != 0:
    num1 = int(input('Digite um número [0 para finalizar]: '))
    if num1 == 0:
        break
    soma += num1
    cont += 1
    if cont == 1:
        maior = num1
        menor = num1
    if num1 > maior:
        maior = num1
    elif menor > num1:
        menor = num1

print('foram solicitados {} números.'.format(cont))
print('A soma dos números é {}.'.format(float(soma)))
print('A média dos valores é {:.02f}.'.format(soma/cont))
print('O maior número da lista é {} e o menor é {}'.format(maior, menor))
