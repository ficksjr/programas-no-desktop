# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO


nota1 = float(input('Qual a nota da primeira prova? '))
nota2 = float(input('Qual a nota da segunda prova? '))

media = (nota1+nota2)/2

if media >= 7:
    print('Sua média é {:.01f} e você foi aprovado!'.format(media))
if 5 <= media < 7:
    print('Sua média é {:.01f} e você necessita fazer recuperação!'.format(media))
if media < 5:
    print('Sua média é {:.01f} e você foi reprovado!'.format(media))
