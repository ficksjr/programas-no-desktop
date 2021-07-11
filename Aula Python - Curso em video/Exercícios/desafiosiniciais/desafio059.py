# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print('O que deseja fazer com os números digitados? ')
escolha = int(input('Escolha dentre as opções a seguir e digite o número correspondente: \n[ 1 ] somar\n[ 2 ] '
                    'multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nDigite aqui:'))

while escolha in range(1, 6):
    if escolha == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, soma))
        ct = str(input('Deseja recomeçar? [S/N]:')).strip().upper()
        if ct in 'Ss':
            escolha = int(
                input('Escolha dentre as opções a seguir e digite o número correspondente: \n[ 1 ] somar\n[ 2 ] '
                      'multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nDigite aqui:'))
        else:
            break
    elif escolha == 2:
        prod = num1 * num2
        print('O produto entre {} e {} é igual a {}'.format(num1, num2, prod))
        ct = str(input('Deseja recomeçar? [S/N]:')).strip().upper()
        if ct in 'Ss':
            escolha = int(
                input('Escolha dentre as opções a seguir e digite o número correspondente: \n[ 1 ] somar\n[ 2 ] '
                      'multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nDigite aqui:'))
        else:
            break
    elif escolha == 3:
        if num1 > num2:
            print('O número {} é maior do que o número {}'.format(num1, num2))
        elif num2 > num1:
            print('O número {} é maior do que o número {}'.format(num2, num1))
        else:
            print('Os números {} e {} são iguais'.format(num1, num2))
        ct = str(input('Deseja recomeçar? [S/N]:')).strip().upper()
        if ct in 'Ss':
            escolha = int(
                input('Escolha dentre as opções a seguir e digite o número correspondente: \n[ 1 ] somar\n[ 2 ] '
                      'multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nDigite aqui:'))
        else:
            break
    elif escolha == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        escolha = int(input('Escolha dentre as opções a seguir e digite o número correspondente: \n[ 1 ] somar\n[ 2 ] '
                            'multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nDigite aqui:'))
    elif escolha == 5:
        print('Você escolheu finalizar')
        break
