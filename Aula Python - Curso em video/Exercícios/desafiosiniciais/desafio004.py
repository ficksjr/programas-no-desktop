t1 = input('Digite alguma coisa:')
print(type(t1))
print('{} é do tipo alfabético?'.format(t1), t1.isalpha())
print('{} é do tipo numérico?'.format(t1), t1.isnumeric())
print('{} é do tipo alfanumérico?'.format(t1), t1.isalnum())
print('{} é um dígito?'.format(t1), t1.isdigit())
print('{} é um decimal?'.format(t1), t1.isdecimal())
print('{} está escrito todo em letras minúsculas?'.format(t1), t1.islower())
print('{} está escrito todo em letras maiúsculas?'.format(t1), t1.isupper())
print('{} é printável?'.format(t1), t1.isprintable())
print('{} é um espaço em branco?'.format(t1), t1.isspace())
