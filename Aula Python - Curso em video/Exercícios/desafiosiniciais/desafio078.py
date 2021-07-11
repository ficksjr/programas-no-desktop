# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
# foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
print(f'O maior valor digitado foi {max(lista)} e a sua posição é a {1+lista.index(max(lista))}ª')
print(f'O menor valor digitado foi {min(lista)} e a sua posição é a {1+lista.index(min(lista))}ª')


