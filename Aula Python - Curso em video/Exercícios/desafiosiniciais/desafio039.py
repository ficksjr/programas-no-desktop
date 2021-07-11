# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
# idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
from time import sleep

dn = int(input('Qual o seu dia de nascimento? '))
mn = int(input('Qual o seu mês (número) de nascimento? '))
an = int(input('Qual o seu ano de nascimento (formato xxxx)? '))

hoje = date.today()

anos = hoje.year - an
meses = hoje.month - mn
dias = hoje.day - dn

if mn == 1 or mn == 3 or mn == 5 or mn == 7 or mn == 8 or mn == 10 or mn == 12:
    dias_no_mes = 31
elif mn == 4 or mn == 6 or mn == 9 or mn == 11:
    dias_no_mes = 30
else:
    dias_no_mes = 28

if mn == 5 or mn == 7 or mn == 10 or mn == 12:
    dias_no_mes_passado = 30
elif mn == 2 or mn == 4 or mn == 6 or mn == 9 or mn == 11:
    dias_no_mes_passado = 30
else:
    dias_no_mes_passado = 28

if meses < 0:
    anos -= 1
    meses += 12
if dias < 0:
    meses -= 1
    dias = dias_no_mes + dias
    if meses < 0:
        anos -= 1
        meses += 12

print('Você tem {} anos, {} meses  e {} dias de vida desde que nasceu.'.format(anos, meses, dias))

if anos == 18:
    print('Se você for do sexo masculino, precisa se alistar este ano ainda. ')
if anos == 17:
    if mn < hoje.month:
        print('Se você for do sexo masculino, precisa se alistar no ano seguinte. ')
    elif mn == hoje.month:
        if dn < hoje.day:
            print('Se você for do sexo masculino, precisa se alistar no ano seguinte. ')
        else:
            print('Se você for do sexo masculino, precisa se alistar neste ano. ')
    else:
        print('Se você for do sexo masculino, precisa se alistar neste ano. ')
if anos > 18:
    print('Se você for do sexo masculino, já cumpriu com suas obrigações militares?. ')
    print('Se cumpriu, parabéns! Se não cumpriu ainda, regularize a sua situação. ')
if anos < 17:
    print('Você não precisa se preocupar em se alistar por enquanto. Volte para o colégio. ')
    print('Preocupe-se em se alistar no ano em que completar 18 anos')


exit(sleep(2))
