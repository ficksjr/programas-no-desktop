# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado

sal = float(input('Salário: '))
imo = float(input('Imóvel: '))
ano = float(input('Anos : '))
compr = sal * 0.3
prest = imo / (ano*12)
if compr > prest:
    print(prest)
else:
    print('aumente o prazo')
