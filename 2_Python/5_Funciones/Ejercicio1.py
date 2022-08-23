def areaTriagunlo(base, altura):
    return (base * altura) / 2

def areaCirculo(radio):
    return 3.1416 * (radio ** 2)

print(areaTriagunlo(int(input("Ingrese la base del triangulo: ")), int(input("Ingrese la altura del triangulo: "))))
print(areaCirculo(int(input("Ingrese el radio del circulo: "))))