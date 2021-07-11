# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if 18 <= idade < 70:
        return f'Votar com {idade} anos é obrigatório.'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Votar com {idade} anos é facultativo.'
    elif idade < 16:
        return f'Votar com {idade} anos é proibido.'


ano_nasc = int(input('Qual o seu ano de nascimento? -> '))
print('-'*len(voto(ano_nasc)))
print(voto(ano_nasc))
print('-'*len(voto(ano_nasc)))
