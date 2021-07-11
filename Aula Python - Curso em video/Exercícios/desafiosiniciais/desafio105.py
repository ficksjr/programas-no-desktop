# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*n, sit=False):
    """
    :
    : Função criada com objetivo de receber vários valores de notas de alunos.
    : É criado condições para:
    :    -   contar o número de valores cadastrados e atibuir o valor ao CONT.
    :    -   atribuir o maior valor imputado e guardar na variável "maior".
    :    -   atribuir o menor valor imputado e guardar na variável "menor".
    :    -   calcular a média de todas as notas e guardar na variável "media".
    :    -   situação (opcional) caso queira saber da situação geral da turma de acordo com:
    :        * ÓTIMA para média acima OU igual a 9.
    :        * BOM para média acima OU igual a 7.5 E menores do que 9.
    :        * OK para média acima OU igual a 6 E menores do que 7.5.
    :        * RUIM para média abaixo de 6.
    :
    """
    maior = 0
    menor = 0
    soma = 0
    cont = 0

    for i in n[0]:
        cont += 1
        soma += i
        if cont == 1:
            maior = i
            menor = i
        elif i > maior:
            maior = i
        elif i < menor:
            menor = i
    media = soma/cont
    notas_garimpo = {'num_notas': cont, 'maior_nota': maior, 'menor_nota': menor, 'media_turma': media}
    print(notas_garimpo)
    if sit:
        if media >= 9:
            print('A situação da turma é ótima!')
        elif 7.5 <= media < 9:
            print('A situação da turma é boa.')
        elif 6.0 <= media < 7.5:
            print('A situação da turma é OK.')
        elif media < 6:
            print('A situação da turma é ruim')


# main_function
notas_alunos = []
while True:
    notas_alunos.append(float(input('Nota:')))
    esc = str(input('Deseja cadastrar mais notas? [S/N]')).strip().lower()
    if esc in 'n':
        break

notas(notas_alunos, sit=True)
