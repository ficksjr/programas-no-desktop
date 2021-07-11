# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista_grande = []
lista_pequena =[]

cont_p = 0
leve = 0
pesada = 0

while True:
    lista_pequena.append(str(input('Nome: ')))
    lista_pequena.append(int(input('Peso [Kg]: ')))
    lista_grande.append(lista_pequena[:])
    lista_pequena.clear()
    esc = str(input('Deseja Continuar? [S/N]: '))
    if esc in 'Nn':
        break
print(f'O número de pessoas cadastradas é {len(lista_grande)}')
for listinha in range(0, len(lista_grande)):
    if listinha == 0:
        leve = pesada = lista_grande[0][1]
    elif listinha > 0:
        if lista_grande[listinha][1] > pesada:
            pesada = lista_grande[listinha][1]
        if lista_grande[listinha][1] < leve:
            leve = lista_grande[listinha][1]
print('A(s) pessoa(s) mais pesada(s) é(são): ', end='')
for i in lista_grande:

    if i[1] == pesada:
        print(f'[{i[0]}] ',end='')
print('\nA(s) pessoa(s) mais leve(s) é(são): ', end='')
for i in lista_grande:
    if i[1] == leve:
        print(f'[{i[0]}] ', end='')
