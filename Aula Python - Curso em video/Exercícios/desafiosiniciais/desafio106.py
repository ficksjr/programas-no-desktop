# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
# comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use
# cores.

def ihelp(a="none"):
    print(f'\033[1;30;47m', end='')
    help(a)
    print(f'\033[0m', end='')


# main_function
while True:
    x = str(input('\033[1;31;40m Qual comando deseja ajuda? ->'))
    ihelp(x)
    esc = str(input('\033[3;30;44m Deseja utilizar novamente [S/N]? ->')).strip().lower()
    if esc in 'n':
        print("\033[3;35;40mFIM!")
        break
