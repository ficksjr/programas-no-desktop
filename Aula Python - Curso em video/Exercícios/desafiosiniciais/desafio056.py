# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
idade = 0
soma_idade = 0
idade_velho = 0
nome_velho = ''
cont = 0
contm = 0

for i in range(1, 5):
    print('---- {}ª pessoa ----'.format(i))
    nome = str(input('Nome? : ')).strip()
    idade = int(input('Idade? : '))
    sexo = str(input('Gênero é M/F? : ')).strip().upper()
    soma_idade += idade
    media = soma_idade / i
    if sexo == 'M' and cont == 0:
        nome_velho = nome
        idade_velho = idade
        cont += 1
    if sexo == 'M' and cont >= 1:
        if idade > idade_velho:
            nome_velho = nome
            idade_velho = idade
    if sexo == 'F' and idade < 20:
        contm += 1

print('A média de idade entre o grupo é {} anos'.format(media))
print('O homem mais velho tem {} e se chama {}'.format(idade_velho, nome_velho))
print('Há {} mulher(es) com menos de 20 anos.'.format(contm))
