import pickle


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
# crear objeto y guardarlo en un fichero binario
ob = Vehiculo('Audi', 'A4')
fichero = open('vehiculo.bin', 'wb')
pickle.dump(ob, fichero)
fichero.close()

# leer el objeto del fichero binario
fichero = open('vehiculo.bin', 'rb')
ob2 = pickle.load(fichero)
fichero.close()

print(f'Marca objeto 1: {ob.marca}')
print(f'Modelo objeto 1: {ob.modelo}')
print(f'Marca objeto 2: {ob2.marca}')
print(f'Modelo objeto 2: {ob2.modelo}')

