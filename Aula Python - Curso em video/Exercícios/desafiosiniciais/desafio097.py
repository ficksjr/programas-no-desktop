# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    compr = len(txt)
    print('#'*compr)
    print(f'{txt}')
    print('#' * compr)


texto = str(input('Digite uma frase curta: '))
escreva(texto)
