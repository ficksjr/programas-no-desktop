# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.

num = int(input('Quer saber a tabuada do seu número? digite ele aqui: '))
for i in range(1,11):
    print('{} X {} = {}'.format(num, i, num*i))
