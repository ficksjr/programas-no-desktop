# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


name = str(input('Nome do jogador: ')).strip().capitalize()
gol = input('Quantidade de gols feita no campeonato: ')

if name.isalpha() is False and gol.isnumeric() is False:
    ficha()
if name.isalpha() is True and gol.isnumeric() is False:
    ficha(nome=name)
if name.isalpha() is False and gol.isnumeric() is True:
    ficha(gols=gol)
if name.isalpha() is True and gol.isnumeric() is True:
    ficha(name, gol)