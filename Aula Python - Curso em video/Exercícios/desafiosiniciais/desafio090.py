# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {'nome': str(input('Nome do aluno: ')), 'média': float(input('A média do aluno é: '))}

if aluno['média'] < 7:
    print(f'O aluno {aluno["nome"]} tem média {aluno["média"]}')
    print('O status do aluno é REPROVADO!')
else:
    print(f'O aluno {aluno["nome"]} tem média {aluno["média"]}')
    print('O status do aluno é APROVADO!')
