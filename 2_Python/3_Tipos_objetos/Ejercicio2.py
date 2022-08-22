peso = int(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
IMC = peso / (altura ** 2)
#imprimir IMC con 2 decimales
print(f'Su IMC es : %.2f' % IMC)
