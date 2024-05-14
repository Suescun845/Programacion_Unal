import math

### Suma De Cuadrados ### 

def suma_Cuadrados ():
    numero = 1
    suma_Cuadrados_numero = 0
    cantidad_usuario = int(input("Cuantos numeros al cuadrado consecutivos quiere sumar: "))
    while numero <= cantidad_usuario:
        suma_Cuadrados_numero += numero**2
        print(f"El {numero} al cuadrado es: {numero**2} ")
        print(f"La suma de todos los numeros cuadrados mostrados es: {suma_Cuadrados_numero} ")
        numero += 1

### Suma De Raices Cuadradas ###

def suma_raices ():
    numero = 0
    suma_raices_numero = 0
    cantidad_usuario = int(input("Cuantas raices cuadradas consecutivas quiere sumar: "))
    base = int(input("Cual radical desea, debe ser positivo: "))
    if cantidad_usuario < 0 or base <= 0:
        print("Es un numero imaginario, vuelva a digitar otro numero positivo") 
    while numero <= cantidad_usuario:
        suma_raices_numero += numero**(1/base)
        print(f"La raiz con radical {base} de {numero} es: {numero**(1/base)} ")
        print(f"La suma de todas las raices con radical {base} mostrados es {suma_raices_numero} ")
        numero += 1


while True:
    eleccion = int(input("Digite la decision que necesite: \n1)Suma Cuadrados Consecutivos \n 2)Suma Raices Consecutivas \n 3) Salir\n"))
    match eleccion:
        case 1:
            suma_Cuadrados()
            pass
        case 2:
            suma_raices()
            pass
        case 3:
            print("Hasta luego 👋 , Creado por Angel Suescun")
            break
        case _:
            print("Numero Incorrecto")