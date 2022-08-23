class Alumnos:
    nombre = ''
    nota = 0
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return 'El alumno ' + self.nombre + ' tiene una nota de ' + str(self.nota)
    def aprobado(self):
        if self.nota >= 3:
            return 'El alumno ' + self.nombre + ' esta aprobado'
        else:
            return 'El alumno ' + self.nombre + ' esta reprobado'

alumnoA = Alumnos('Juan', 4)
alumnoB = Alumnos('Pedro', 2)
alumnoC = Alumnos('Ana', 5)
print(alumnoA.__str__())
print(alumnoA.aprobado())

print(alumnoB.__str__())
print(alumnoB.aprobado())

print(alumnoC.__str__())
print(alumnoC.aprobado())