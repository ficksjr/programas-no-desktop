# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoa = {}
povo = []
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        try:
            pessoa['idade'] = int(input('Idade: '))
            soma += pessoa['idade']
            break
        except ValueError:
            print('Valor inválido.')
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro: Escolha entre M e F.')
    povo.append(pessoa.copy())
    while True:
        esc = str(input('Deseja continuar? [S/N]')).strip().upper()
        if esc in 'SN':
            break
    if esc in 'N':
        break

print(f'Foram cadastradas {len(povo)} pessoas.')
media = (soma / (len(povo)))
print(f'A média de idade é {media:.02f} anos.')
print('As mulheres cadastradas são:')
for p in povo:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end='. ')
print('\nAs pessoas com idade acima da média foram: ')

for pv in povo:
    if pv["idade"] > media:
        print(f'{pv["nome"].capitalize()} com {pv["idade"]} anos.', end='. ')
