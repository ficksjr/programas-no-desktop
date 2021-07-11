# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.


s = str(input('Me diga uma cidade do Brasil: '))

s = s.lower()

print(s.startswith('santo'))
