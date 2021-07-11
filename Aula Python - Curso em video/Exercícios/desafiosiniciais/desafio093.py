# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}
gol = []
dados['nome'] = str(input('Nome: ')).strip().capitalize()
jogos = int(input('Número de partidas: '))
dados['partidas'] = jogos
for i in range(0, jogos):
    gol.append(int(input(f'Na partida {i+1} fez quantos gols? ')))
    soma = sum(gol)
dados['gols'] = gol
dados['totalgols'] = soma
print(dados)
