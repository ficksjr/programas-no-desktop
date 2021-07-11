# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso
# esteja errado, peça a digitação novamente até ter um valor correto.

sx = str(input('Qual é o seu gênero? [M/F] ')).upper().strip()
print(sx)
print(type(sx))
while sx not in 'MmFf':
    print('Digite somente M ou F.')
    sx = str(input('Novamente. Qual é o seu gênero? [M/F] ')).upper()

print('Obrigado, tenha uma boa semana!')