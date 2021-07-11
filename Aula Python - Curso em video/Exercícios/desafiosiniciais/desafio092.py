# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com
# idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

pessoa = {}

pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
pessoa['nascimento'] = int(input('Ano de nascimento [xxxx]: '))
pessoa['contribuicao'] = int(input('Anos de contribuição: '))
pessoa['salario'] = int(input('Último salário: '))
pessoa['idade'] = date.today().year - pessoa['nascimento']

if pessoa['sexo'] in 'mM':
    pessoa['aposenta'] = int(((100 - pessoa['idade'] - pessoa['contribuicao'])/2) + pessoa['idade'])

if pessoa['sexo'] in 'fF':
    pessoa['aposenta'] = int(((90 - pessoa['idade'] - pessoa['contribuicao'])/2) + pessoa['idade'])

print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos e irá se aposentar com {pessoa["aposenta"]} anos.')