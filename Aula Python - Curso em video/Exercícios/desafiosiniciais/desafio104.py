# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite
# um n: ‘)

def leiaint(n):
    if n.isnumeric() is not True:
        print(f'"{n}" não é um número inteiro.')
    else:
        print(f'"{n}" é um número inteiro.')


coisa = input('Digite algo: ')
leiaint(coisa)
