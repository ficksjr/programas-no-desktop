# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a1 = 'Pedro'
a2 = 'Henrique'
a3 = 'Marcos'
a4 = 'Gustavo'
alunos = [a1, a2, a3, a4]
print('O aluno sorteado pelo professor para apagar o quadro é: {}!'.format(random.choice(alunos)))
