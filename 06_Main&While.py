### Repaso Main ###

import math

def suma(a,b):
        return a+b

def raiz2 (n):
    if (n>=0):
        return math.sqrt(n)
    else:
        print(f"La raiz cuadrada de {n} es un numero imaginario")
        
def main():
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo numero: "))
    print(f"La suma entre {x,y} es: {suma(x,y)}")
    print(f"La riz cuadrada de {x} es: {raiz2(x)}")

main()

### Ciclos ###

### Impar ###

impar = 1
suma_Impar = 0
cantidad = 1
cantidad_usuario = int(input("Cuantos numeros impares quiere sumar: "))
while cantidad <= cantidad_usuario:
    print(f"El {cantidad} numero impar es: {impar} ")
    suma_Impar = suma(suma_Impar, impar)
    impar += 2
    cantidad += 1
    print(f"La suma de todos los numeros impares mostrados es {suma_Impar} ")

print(f"La suma de todos los numeros impares hasta la posición {cantidad_usuario} es: {suma_Impar} ")

### Par ###

par = 0
suma_Par = 0
cantidad = 1
cantidad_usuario = int(input("Cuantos numeros pares quiere sumar: "))

while cantidad <= cantidad_usuario:
    print(f"El {cantidad} numero par es: {impar} ")
    suma_Par = suma(suma_Par, par)
    par += 2
    cantidad += 1
    print(f"La suma de todos los numeros pares mostrados es {suma_Par} ")

print(f"La suma de todos los numeros pares hasta la posición {cantidad_usuario} es:{suma_Par} ")

### Fibonacci ###

fibo = 0
suma_fibo = 1
suma_fibo2 = 0
cantidad = 1
suma_total = 0
cantidad_usuario = int(input("Cuantos numeros pares quiere sumar: "))

while cantidad <= cantidad_usuario:
    print(f"El {cantidad} numero de la serio de Fibonacci es: {fibo} ")
    suma_fibo2 = suma(suma_fibo, fibo) 
    suma_total = suma(fibo, suma_total)
    fibo = suma_fibo
    suma_fibo = suma_fibo2
    cantidad += 1
    print(f"La suma de todos los numeros pares mostrados es {suma_total} ")


### Tarea c.10 suma de cuadrados y raices 20 y fibonacci