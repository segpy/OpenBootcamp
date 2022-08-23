class Vehiculo:
    color = ''
    ruedas = 0
    puertas = 0

# clase coche hereda de vehiculo
class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

coche = Coche()
coche.color = 'rojo'
coche.ruedas = 4
coche.puertas = 4
coche.velocidad = 200
coche.cilindrada = 1600
print('El color del coche es: ' + coche.color)
print('El numero de ruedas del coche es: ' + str(coche.ruedas))
print('El numero de puertas del coche es: ' + str(coche.puertas))
print('La velocidad del coche es: ' + str(coche.velocidad))
print('La cilindrada del coche es: ' + str(coche.cilindrada))