# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O
# programa encerrará quando ele disser que quer mostrar 0 termos.

pt = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a razão da PA: '))

numtermos = 0
print('Os 10 primeiros termos desta PA são:')
while numtermos < 10:
    print('{}'.format(pt + numtermos * ra), end='')
    print(', ' if numtermos < 9 else '.', end='')
    numtermos += 1
numtermos = 0
resp1 = str(input('\nDeseja ver mais termos? [S/N] ')).strip().upper()
if resp1 in 'S':
    ta = int(input('Quantos termos adicinais quer adicionar? '))
    print('Os {} primeiros termos desta PA são:'.format(10+ta))
    while numtermos < 10+ta:
        print('{}'.format(pt + numtermos * ra), end='')
        print(', ' if numtermos < 9+ta else '.', end='')
        numtermos += 1
elif resp1 not in 'S':
    print('Obrigado por utilizar o gerador de PA.')
