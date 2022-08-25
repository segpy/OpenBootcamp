#importar reduce
from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]
impares = list(filter(lambda x: x%2 != 0, lista))
print('Impares:', list(impares))
suma = reduce(lambda x,y: x+y, impares)
print('Suma:', suma)
