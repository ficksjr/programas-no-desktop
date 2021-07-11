dias = float(input('Por quantos dias pretende alugar o carro?'))
km = float(input('Quantos quilômetros pretende percorrer?'))
preco = 60*dias + 0.15*km

print('O valor do aluguel sairá no total R$ {:.02f}'.format(preco))
