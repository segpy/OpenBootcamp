paises = input('Ingrese la lista de paises separados por comas: ').split(',')
paisesUnicos = set(paises)
#ordenar lista de paises
paisesOrdenados = sorted(paisesUnicos)
print('Lista de paises:')
for pais in paisesOrdenados:
    if pais == paisesOrdenados[-1]:
        print(pais)
    else:
        print(pais, end=', ')
