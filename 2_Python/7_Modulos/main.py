import operaciones as op

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
#mostrar que metodos hay disponibles
print('Metodos: ',[item for item in dir(op) if '__' not in item])

print("La suma es: " , op.suma(a,b))
print("La resta es: " , op.resta(a,b))
print("La multiplicacion es: " , op.multiplicacion(a,b))
print("La division es: " , op.division(a,b))
