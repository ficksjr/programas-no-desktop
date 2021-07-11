# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No
# final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
       int(input('Digite outro número: ')), int(input('Digite outro número: ')))

if num.count(9) > 0:
    print(f'O número 9 apareceu {num.count(9)} vez(es).')
else:
    print('O número 9 não foi digitado')
if num.count(3) > 0:
    print(f'O número 3 apareceu, por primeiro, na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado')

# if num.count(2) > 0 or num.count(4) > 0 or num.count(6) > 0 or num.count(8) > 0 or num.count(0) > 0:
#    print(f'O(s) número(s) par(es) é(são): ')
#    for i in range(0, 4):
#        if num[i] % 2 == 0:
#            print(num[i], end=' ')
# else:
#    print('Não foram digitados números pares.')

print('Foram digitados os ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('Nenhum')
