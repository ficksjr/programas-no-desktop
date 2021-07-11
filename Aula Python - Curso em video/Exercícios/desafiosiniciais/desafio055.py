# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
# peso lidos.

pp = []

for i in range(1, 6):
    pp.append(int(input('Digite o peso da {}ª pessoa, em Kg: '.format(i))))
    pp.sort()

print('A pessoa mais pesada é a pessoa que pesa {} kg.]'.format(pp[len(pp)-1]))
print('A pessoa mais leve é a pessoa que pesa {} kg.]'.format(pp[0]))
