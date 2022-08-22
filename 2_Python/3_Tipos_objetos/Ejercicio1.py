nombre = 'Sebastian'
apellidos = 'Gomez'
edad = '23'
email = 'sebasgv@correo.com'
telefono = '123456789'
casado = False
conHijos = False
listaAmigos = ['Sebastian', 'Juan', 'Pedro', 'Maria', 'Luis', 'Ana']
peliculasVistas = {'Pelicula1': '2012', 'Pelicula2': 'Spiderman', 'Pelicula3': 'El señor de los anillos'}

print('Hola, mi nombre es', nombre, apellidos, 'y tengo', edad, 'años')
print('Mi email es', email)
print('Mi telefono es', telefono)
print('Mi situacion sentimental es', 'casado' if casado else 'soltero')
print('Tengo', 'hijos' if conHijos else 'no tengo hijos')
print('Mis amigos son:')
print(*listaAmigos, sep=', ')
print('Mis peliculas vistas son:')
for pelicula in peliculasVistas:
    print(pelicula, ':', peliculasVistas[pelicula])
