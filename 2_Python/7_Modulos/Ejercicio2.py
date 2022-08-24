from datetime import datetime as dt

#print([metodo for metodo in dir(dt) if '__' not in metodo])

horaActual = dt.now()
formatoFecha = "%Y-%m-%d"
formato = "%Y-%m-%d %H:%M:%S"
#print(dt.strftime(horaActual.date(),formatoFecha)+" 19:00:00")
horaSalida = dt.strptime(dt.strftime(horaActual.date(),formatoFecha)+" 19:00:00", formato)
#print(horaActual.date())
hora1 = dt.strptime(dt.strftime(horaActual.date(),formatoFecha)+' '+input('Ingrese hora de prueba1 (H:M:S): '), formato)
hora2 = dt.strptime(dt.strftime(horaActual.date(),formatoFecha)+' '+input('Ingrese hora de prueba1 (H:M:S): '), formato)
#print(type(hora1-hora2)) #type(hora1-hora2) es un timedelta
# programa que verifica si una hora es mayor a la otra
def mayor(hora2, hora1=horaSalida):
    if hora2.time() > hora1.time():
        return 'Ya salio de la hora laboral'
    else:
        return 'Le quedan ' + str(hora1 - hora2) + ' para salir de la hora laboral'
print(mayor(hora1))
print(mayor(hora2))
print(mayor(horaActual))
