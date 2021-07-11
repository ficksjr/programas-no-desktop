# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

cont_18 = 0
cont_masc = 0
cont_fem20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo. [M/F]')).strip().upper()
    if idade >= 18:
        cont_18 += 1
    if sexo in 'Mm':
        cont_masc += 1
    if sexo in 'Ff' and idade < 20:
        cont_fem20 += 1
    esc = str(input('Deseja imputar mais dados: [S/N]')).strip().upper()
    if esc in 'Nn':
        break
print(f'Há {cont_18} pessoas maiores de idade.')
print(f'Há {cont_masc} pessoas do sexo masculino cadastradas.')
print(f'Há {cont_fem20} pessoas do sexo feminina menores de 20 anos.')
