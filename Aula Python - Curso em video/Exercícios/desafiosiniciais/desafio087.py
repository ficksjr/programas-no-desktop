# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

s_par = 0
s_ter = 0
maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = (int(input(f'Digite um número para o item [{linha},{coluna}]: ')))
        matriz[linha][coluna] = num
        if num % 2 == 0:
            s_par += num
        s_ter += matriz[linha][2]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()

print(f'A soma dos valores pares é = {s_par}')
print(f'A soma dos valores da terceira coluna é = {s_ter}')
print(f'O maior valor da segunda linha é = {max(matriz[1])}')
