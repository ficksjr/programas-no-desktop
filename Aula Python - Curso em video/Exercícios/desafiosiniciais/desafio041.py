# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

from datetime import date

ano_atual = date.today().year


ano_nascimento = int(input('Qual o ano de seu nascimento (formato xxxx)?'))

idade = ano_atual - ano_nascimento

print(idade)

if idade < 9:
    print('Você tem {} ano(s) e sua categoria é a MIRIM'.format(idade))
elif 9 <= idade < 14:
    print('Você tem {} ano(s) e sua categoria é a INFANTIL'.format(idade))
elif 14 <= idade < 19:
    print('Você tem {} ano(s) e sua categoria é a JÚNIOR'.format(idade))
elif 19 <= idade < 25:
    print('Você tem {} ano(s) e sua categoria é a SÊNIOR'.format(idade))
elif idade > 25:
    print('Você tem {} ano(s) e sua categoria é a MASTER'.format(idade))
