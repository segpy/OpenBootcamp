def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap
year = int(input("Ingrese un año: "))
if is_leap(year):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")