### Strings ###

cadena = "Universidad Nacional De Colombia"
cadena2 = "Facultad de ingenieria"
cadena3 = "Hola"
cadena4 = " hola"
cadena5  = "1234567876543"

print(f"Longitud de la cadena 1 es: {len(cadena)}")
print(f"Longitud de la cadena 2 es: {len(cadena2)}")
print(f"Longitud de la cadena 3 es: {len(cadena3)}")
print(f"Longitud de la cadena 4 es: {len(cadena4)}")
print(f"Es mayor la cadena 4 que la cadena 3: {cadena4 > cadena3}")
print(f"Son iguales las cadenas 3 y 4: {cadena3 == cadena4}")
print(f"Concatenar la cadena 1 y cadena 2 {cadena + cadena2}")
print(f"Concatenar la cadena 1 y cadena 2 {cadena, cadena2}")
print(f"Concatenar el primer caracter de las cadena 1 y cadena 2 {cadena[0], cadena2[0]}")
print(f"Concatenar el noveno caracter de la cadena 1 y cadena 2 {cadena[9], cadena2}")

if "si" in cadena:
    print("Si esta en la cadena 1")
else:
    print("No esta en la cadena")

for i in cadena2:
    print(i, end=", ")

### Manejo de Cadenas ###

print(f"Primeros 5 subindices de la cadena 1: {cadena[:5]}")
print(f"Subindices del 9 caracter hasta el caracter 22 de la cadena 1: {cadena[9:22]}")
print(f"Cadena 1 invertida: {cadena[::-1]}")
print(f"Cuenta cuantos si hay en la cadena 1: {cadena.count('si')}")
print(f"Cuenta cuantos i hay en la cadena 1: {cadena.count('i')}")
print(f"Cuantos caracteres hay antes de 'si' en la cadena 1: {cadena.find('si')}")
print(f"Cuenta cuantos caracteres hay despues de 'si' en la cadena 1: {cadena.rfind('si')}")

cadena = "iiiiiiiiiiiiiiiiiiiiiUniversidad Nacional De Colombiaiiiiiiiiiiiii"

print(f"quita las i que hay a los lados en la cadena 1: {cadena.strip('i')}")
print(f"quita las i de la derecha en la cadena 1: {cadena.lstrip('i')}")
print(f"quita las i de la derecha en la cadena 1: {cadena.lstrip('i')}")

cadena = "Universidad Nacional De Colombia"

print(f"Justifica la cadena a la izquierda: {cadena.ljust(10, "-")}")
print(f"Justifica la cadena a la derecha: {cadena.rjust(10, '-')}")
print(f"Centra la cadena: {cadena.center(10, '-')}")
print(f"Llena una cadena de ceros: {cadena5.zfill(20)}")


#documento, edad, nacimiento, split


'''
Ejercicio
'''

palabras = cadena.split()
print(palabras)

cadena6 = "En el ejemplo anterior, cadena.split() divide la cadena en palabras individuales, u"

palabras = cadena6.split(",")
print(palabras)

palabras = cadena6.split(",", 1)
print(palabras)

info_personal = "Angel Suescun, 18, 31/08/2005, 1029141516, Masculino"

palabras = info_personal.split(",")
print(f"Nombre:{palabras[0]} ,Edad:{palabras[1]} años, fecha de nacimiento: {palabras[2]},Cedula:{palabras[3]} ,Sexo:{palabras[4]}")

info_personal = str(input("Por favor, digite en una sola linea su nombre, edadm fecha de nacimiento, cedula y sexo, todo separado por comas.\n Ejemplo: nombre, edad, fecha, cedula, sexo:\n"))
palabras = info_personal.split(",")
print(f"Nombre:{palabras[0]} ,Edad:{palabras[1]} años, fecha de nacimiento: {palabras[2]},Cedula:{palabras[3]} ,Sexo:{palabras[4]}")

nombre, edad, fecha, cedula, sexo =str(input("Por favor, digite en una sola linea su nombre, edadm fecha de nacimiento, cedula y sexo, todo separado por comas.\n Ejemplo: nombre, edad, fecha, cedula, sexo:\n")).split(",")
print(f"Nombre:{nombre} ,Edad:{edad} años, fecha de nacimiento: {fecha},Cedula:{cedula} ,Sexo:{sexo}")
