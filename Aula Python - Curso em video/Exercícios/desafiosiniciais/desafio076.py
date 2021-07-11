lista = ('Abacaxi', 3.,
         'Pera', 6.5,
         'Uva', 5.5,
         'Banana', 8.9,
         'Beterraba', 7.9,
         'Macarrão', 2.5,
         'Carne', 45.)

print('='*37)
print(f'{"Lista de Preços":^37}')
print('='*37)

for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]}', end='')
        print('.' * (36 - len(lista[i]) - 7), end='')
        print(f'R$ {lista[i+1]: >5.02f}')
