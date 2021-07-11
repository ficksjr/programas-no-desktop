# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários dados_jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada dados_jogador.

# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
# nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No
# final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados_jogador = {}
jogadores = []
gols = []

while True:
    dados_jogador.clear()
    soma = 0
    dados_jogador['nome'] = str(input('Nome do jogador: ')).strip().upper()
    while True:
        try:
            jogos = int(input('Partidas disputadas: '))
            dados_jogador['partidas'] = jogos
            if jogos >= 1:
                break
        except ValueError:
            print('Valor inválido.')
    for jogos in range(0, jogos):
        gols.append(int(input(f'Na partida {jogos + 1} fez quantos gols? ')))
        soma += gols[jogos]
    dados_jogador['gol'] = gols[:]
    dados_jogador['total_gols'] = soma
    dados_jogador['media'] = dados_jogador['total_gols']/dados_jogador['partidas']
    jogadores.append(dados_jogador.copy())
    gols.clear()
    while True:
        esc = str(input('Deseja continuar? [S/N]')).strip().upper()
        if esc in 'SN':
            break
    if esc in 'N':
        break

print(f'Foram cadastrados {len(jogadores)} jogadores:')

while True:
    esc = str(input('Deseja acessar os dados de algum jogador específico? [S/N]: ')).strip().upper()
    if esc in 'N':
        break
    elif esc in 'S':
        for jogador in jogadores:
            print(f'({jogadores.index(jogador)}) {jogador["nome"]}')
        while True:
            try:
                indice = int(input('De acordo com o índice do jogador à esquerda, digite o índice do jogador que '
                                   'queira consultar: '))
                if indice >= 0:
                    print(f'O jogador {jogadores[indice]["nome"]} tem {jogadores[indice]["total_gols"]} gol(s)'
                          f' em {jogadores[indice]["partidas"]} partida(s) disputada(s) '
                          f'totalizando {jogadores[indice]["media"]:.02f} gol(s) por partida')
                    for i in range(0, jogadores[indice]["partidas"]):
                        print(f'Na partida {i+1} marcou {jogadores[indice]["gol"][i]} gol(s).')
                break
            except ValueError and indice <= 0:
                print('Valor inválido.')
    else:
        print('Você digitou um dado inválido, digite somente "S" ou "N".')
