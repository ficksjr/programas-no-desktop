# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
# espaços. Exemplos de palíndromos:

frase = str(input('Digite a frase: ')).strip().upper()

frase_separada = frase.split()
print(frase_separada)
frase_junta = ''.join(frase_separada)
print(frase_junta)
inverso = ''

for letra in range(len(frase_junta)-1, -1, -1):
    inverso += frase_junta[letra]
print('{}'.format(inverso))

if inverso == frase_junta:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')
