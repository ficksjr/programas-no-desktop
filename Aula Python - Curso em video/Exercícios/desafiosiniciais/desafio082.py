# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao
# final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    esc = str(input('Deseja continuar adicionando números? [S/N]: '))
    if esc in 'nN':
        break
print(lista)
print(lista_par)
print(lista_impar)
