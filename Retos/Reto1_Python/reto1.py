#%%
import pandas as pd
archivo = input("Ingrese el nombre del archivo: ")
path = archivo+".xlsx"
# Read the file
df = pd.read_excel(path)
while True:
    try:
        print('Ingrese el nombre de la columna que desea filtrar: ', end=' ')
        # Read the column name
        columna = input()
        filtro = df[columna]
        break
    except:
        print('Columna no encontrada')
print('Desea mostrar los datos con duplicado (Y) o sin duplicado (N): ', end='')
duplicado = input()
if duplicado == 'Y':
    print(filtro)
elif duplicado == 'N':
    print(filtro.drop_duplicates())

#Test
correos = pd.DataFrame(df['Correo']).drop_duplicates()
print('Correos con duplicados:\n', df['Correo'], sep='')
print('Correos sin duplicados:\n', correos)

#Pruebas metodos dataframe
#leer columna nomnbre
nombre = pd.DataFrame(df['Nombre'])
#contar duplicados
duplicadosNombre = df['Nombre'].value_counts()
#ordernar alfabeticamente
duplicadosNombre = duplicadosNombre.sort_index()
print('Nombres con duplicados:\n', duplicadosNombre, sep="")