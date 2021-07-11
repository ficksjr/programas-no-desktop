def leiadinheiro(txt):
    validacao = False
    while not validacao:
        recebe = str(input(txt)).replace(",", ".").strip()
        if recebe.isalpha() or recebe == "":
            print(f'Erro: {recebe} não é um valor válido.')
        else:
            validacao = True
            return float(recebe)
