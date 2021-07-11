# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.

print('Para formar um triângulo é necessário possuir três retas de comprimento maior que zero')
reta1 = float(input('Para isso, informe o comprimento da primeira reta: '))
reta2 = float(input('Agora informe o comprimento da segunda reta: '))
reta3 = float(input('Por último informe o comprimento da terceira reta: '))

if reta1 > reta2 and reta1 > reta3:
    maior = reta1
    soma_menores = reta2 + reta3
if reta2 > reta1 and reta2 > reta3:
    maior = reta2
    soma_menores = reta1 + reta3
if reta3 > reta1 and reta3 > reta2:
    maior = reta3
    soma_menores = reta2 + reta1

if maior < soma_menores:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')
