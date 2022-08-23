def numeroPrimo (numero):
    if numero % 2 != 0:
        return True

a = int(input("Ingrese un numero: "))
if numeroPrimo(a):
    print("El numero es primo")
else:
    print("El numero no es primo")


