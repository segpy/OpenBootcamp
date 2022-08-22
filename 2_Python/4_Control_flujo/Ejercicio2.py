inicio = int(input("Ingrese el numero de inicio: "))
fin = int(input("Ingrese el numero de fin: "))
impares = []
for i in range(inicio, fin + 1):
    if i % 2 != 0:
        impares.append(i)
print(impares)
