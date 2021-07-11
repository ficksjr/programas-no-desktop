# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o seu salário? '))

if sal > 1250:
    print('Seu novo salário após aumento será de R${:.02f}'.format(sal * 1.1))
else:
    print('Seu novo salário após aumento será de R${:.02f}'.format(sal * 1.15))

