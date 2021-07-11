# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))

esc = int(input('Escolha qual será a base de conversão:\n1 para binário;\n2 para octal;\n3 para hexadecimal.\n'))

if esc == 1:
    bi = bin(num)
    print(bi[2:])
elif esc == 2:
    oc = oct(num)
    print(oc[2:])
elif esc == 3:
    hexa = hex(num)
    print(hexa[2:])
else:
    print('Você não escolheu o formato de conversão. ')
