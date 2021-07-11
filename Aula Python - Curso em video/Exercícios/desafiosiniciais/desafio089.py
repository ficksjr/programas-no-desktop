# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
# composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
# cada aluno individualmente.

turma = []

while True:
    turma.append([input('Informe o nome do aluno: ').strip().upper(), int(input('Informe a primeira nota: ')),
                  int(input('Informe a segunda nota: '))])
    esc = str(input('Deseja Continuar? [S/N]: '))
    if esc in 'Nn':
        break

soma_notas = 0
print(f'O boletim geral de todos os alunos ficou:')
for indices in range(0, len(turma)):
    soma_notas += turma[indices][1] + turma[indices][2]
    print(f'{turma[indices][0].lower().capitalize()}: P1 = {turma[indices][1]} e P2 = {turma[indices][2]}, '
          f'média = {(turma[indices][1]+turma[indices][2])/2}')

print(f'A turma é composta por {len(turma)} alunos.')
print(f'A média de todos os alunos ficou em: {soma_notas/(2*len(turma)):.01f}.')

cont = 0
while True:
    aluno = str(input('De qual aluno você deseja ver as notas? ')).strip().upper()
    for c in range(0, len(turma)):
        if aluno in turma[c][0]:
            print(f'O aluno {aluno} tirou as seguintes notas: {turma[c][1]} e {turma[c][2]} ')
        elif aluno not in turma[c][0]:
            cont += 1
        if cont == len(turma):
            print(f'O aluno {aluno} não consta na lista da turma.')
            cont = 0
    esc2 = str(input('Deseja ver a nota de mais algum aluno? ')).strip().upper()
    if esc2 in 'N':
        break
print('FIM')
