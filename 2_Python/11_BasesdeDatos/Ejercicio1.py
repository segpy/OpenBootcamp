import mysql.connector

def main():
    conexion = conectar()
    print('Conexion exitosa')
    while conexion.is_connected():
        n = int(input('Cuantos alumnos desea agregar?: '))
        for i in range(n):
            print('Alumno', i+1)
            agregarAlumno(i+1)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM alumnos')
        res = cursor.fetchall()
        for fila in res:
            print(fila)
        conexion.close()


def conectar():
    conexion = mysql.connector.connect(user='root', password='123456789', host='localhost', database='miconexion')
    return conexion

def agregarAlumno(id):
    conexion = conectar()
    cursor = conexion.cursor()
    nombre = input('Ingrese el nombre del alumno: ')
    apellido = input('Ingrese el apellido del alumno: ')
    cursor.execute(f'INSERT INTO alumnos (idAlumnos, nombre, apellido) VALUES ({id}, "{nombre}", "{apellido}")')
    conexion.commit()
    conexion.close()
    print('Alumno agregado')

if __name__ == '__main__':
    main()