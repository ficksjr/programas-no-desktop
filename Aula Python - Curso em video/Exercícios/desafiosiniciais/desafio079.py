# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
# lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = []

while True:
    num = int(input('Digite um número para adicionar à lista: '))
    if num not in lista:
        lista.append(num)
    dec = str(input('Deseja continuar? [S/N]: '))
    if dec in 'Nn':
        break

print(f' os números em ordem crescente são :{sorted(lista)}')
