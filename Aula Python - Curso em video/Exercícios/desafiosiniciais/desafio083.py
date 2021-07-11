# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
# aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

frase = str(input('Digite uma expressão matemática: '))
cont = 0
for letras in frase:
    if '(' in letras:
        cont += 1
    elif ')' in letras:
        cont -= 1
    if cont < 0:
        break
if cont == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')
