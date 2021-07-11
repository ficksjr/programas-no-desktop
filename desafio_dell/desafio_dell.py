# código fonte versão 3.9 Python

import csv  # importando a biblioteca csv para trabalhar este formato no python.

tabela_cidades_distancia = []  # declarando a list 'tabela_cidades_distancia' que constará as cidades e suas
# respectivas distâncias.

with open("DNIT-Distancias.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=";", quoting=csv.QUOTE_ALL)

    # transformando linhas em 'list'.
    for row in reader:
        tabela_cidades_distancia.append(row)

rota = []  # declarando a list 'rota' que constará as rotas entre cidades escolhidas no item #3 do MENU.

soma3 = 0  # declarando a varíavel uniforme para o somatório de kilometragem das rotas do item #3 do MENU.

custoKM = 0

# início do loop
while True:
    print('\n', '=' * 5, 'ESCOLHA UMA OPÇÃO', '=' * 5)
    print('1. Configurar custo por KM')
    print('2. Consultar trecho')
    print('3. Consultar rota')
    print('4. Terminar o programa\n')

    # novo loop para que o valor digitado no menu inicial seja conforme solicitado segundo opções.
    while True:
        try:
            escolha = int(input('Digite a opção aqui: '))
            if escolha not in (1, 2, 3, 4):
                raise ValueError('Valor fora do limite permitido\n')
        except ValueError as e:
            print('Valor inválido: Utilizar somente números de 1 a 4.\n')
        else:
            break

    # configurando escolha de MENU #1 para vir valores de custo positivos e formatos corretos.
    if escolha == 1:
        while True:
            try:
                custoKM = float(input('Informe o custo por KM rodado, em R$: '))
                if custoKM <= 0:
                    raise ValueError('Valor inválido: Utilizar somente números e valores positivos não nulos.\n')
            except ValueError as e:
                print('Valor inválido: Utilizar somente números e valores positivos não nulos.\n')
            else:
                break

    # configurando escolha de MENU #2 para um trecho entre 2 cidades.
    if escolha == 2:
        if custoKM == 0:
            print('Forneça o valor por KM da viagem no item 1 do MENU.\n')
            continue
        origem = str(input('Informe a Cidade de Origem: ').strip().upper())
        destino = str(input('Informe a Cidade de Destino: ').strip().upper())

        # condição caso a cidade de origem não conste na tabela_cidades_distancia, com repetição.
        while origem not in tabela_cidades_distancia[0]:
            print('Erro de digitação, favor não utilizar acentos ou números.')
            origem = str(input('Informe a cidade de origem novamente: ').strip().upper())
        pos_o = tabela_cidades_distancia[0].index(origem)

        # condição caso a cidade de destino não conste na tabela_cidades_distancia, com repetição.
        while destino not in tabela_cidades_distancia[0]:
            print('Erro de digitação, favor não utilizar acentos ou números.')
            destino = str(input('Informe a cidade de destino novamente: ').strip().upper())
        pos_d = tabela_cidades_distancia[0].index(destino)

        # através dos índices da matriz criada 'tabela_cidades_distancia' determinar a distância as cidades do trecho.
        distancia = int(tabela_cidades_distancia[pos_o + 1][pos_d])
        print(f'O custo da Viagem é R$ {custoKM * distancia:.02f}. \n')

    # configurando escolha de MENU #3 para um trecho entre 2 ou mais cidades para um rota.
    if escolha == 3:
        if custoKM == 0:
            print('Forneça o valor por KM da viagem no item 1 do MENU.\n')
            continue
        rota = []
        while len(rota) < 2:

            # adicionando as cidades numa list 'rota'.
            rota = list(input('Digite o nome de duas ou mais cidades, separado por vírgulas e sem acentos: '
                              ).strip().upper().split(','))

            rota = [c.strip() for c in rota]
            for cidade in rota:
                if cidade not in tabela_cidades_distancia[0]:
                    print(f'A Cidade {cidade} não consta na lista.')
                    rota = []

        # definindo a posição de cada cidade na tabela conforme posição na list 'tabela_cidades_distancia'
        for i in range(0, len(rota) - 1):
            origem_i = rota[i]
            print(f'Entre {origem_i}', 'e ', end='')
            destino_i = rota[i + 1]
            print(f'{destino_i}', end=' ')

            # definindo o índice posição da cidade de origem na tabela das cidades
            pos_o = tabela_cidades_distancia[0].index(origem_i)

            # definindo o índice posição da cidade de destino na tabela das cidades
            pos_d = tabela_cidades_distancia[0].index(destino_i)

            # através dos índices da matriz determinar a distância do trecho entre cada cidade na rota
            distancia_2 = int(tabela_cidades_distancia[pos_o + 1][pos_d])
            soma3 += distancia_2
            print(f' a distância entre as cidades é:  {distancia_2} KM.')

        # calculo do custo do item 3
        print(f'A distância total percorrida na rota é: {soma3} KM.')
        custo_t = soma3 * custoKM

        print(f'O custo total da viagem será de R$ {custo_t:.02f}.')
        litros = soma3 * 2.57

        print(f'Será utilizado {litros:.01f} litros de combustível ao total da rota.')

        print(f'O número de dias para finalizar a viagem será de aproximadamente {soma3 / 283:.0f} dias.\n')
        soma3 = 0

    if escolha == 4:  # término do loop
        break

print('Fim do programa!')
