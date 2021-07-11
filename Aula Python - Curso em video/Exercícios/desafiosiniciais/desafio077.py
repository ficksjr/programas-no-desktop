# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('crie', 'um', 'programa', 'que', 'tenha', 'uma', 'tupla', 'com', 'varias', 'palavras')

for palavra in lista:
    print(f'\nA palavra {palavra} tem as vogais:', end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
