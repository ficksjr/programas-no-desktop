l = float(input('Qual a largura da parede?: '))
h = float(input('Qual a altura da parede?: '))
t = l%h
print('{:.02f}'.format(t))
if t == 0:
    tintas = l*h/2
else:
    tintas = int(l*h/2) + 1
print('Uma parede de {} m de largura por {} m de altura possui:\n{:.2f} metros quadrados e;\nnecessita de {} latas de '
      'tinta'.format(l, h, l*h, tintas))
