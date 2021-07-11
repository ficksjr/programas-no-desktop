def aumentar(n=0, p=1):
    a = n + (n * p / 100)
    return moeda(a)


def diminuir(n=0, p=1):
    di = n - (n * p / 100)
    return moeda(di)


def dobro(n=0):
    do = n * 2
    return moeda(do)


def metade(n=0):
    t = n / 2
    return moeda(t)


def moeda(n=0, cambio="R$"):
    return f'{cambio} {n:.2f}'.replace(".", ",")


def resumo(a=0, b=1, c=1):
    print('-'*34)
    print('RESUMO DA CONTA'.center(34))
    print('-' * 34)
    print(f'Preço analisado: \t\t{moeda(a)}')
    print(f'Aumentado em {b}%: \t{aumentar(a, b)}')
    print(f'Reduzido em {c}%: \t\t{diminuir(a, c)}')
    print(f'O dobro: \t\t\t\t{dobro(a)}')
    print(f'A metade: \t\t\t\t{metade(a)}')
    print('-' * 34)
