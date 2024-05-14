# ### Condicionales ###

# '''
# 1
# '''

# numero=int(input("Ingresa un Numero: "))

# if numero in range(97,123):
#     print("El numero corresponde al caracter (Codigo ASCII):", chr(numero))
# else:
#     print("El numero no corresponde a una letra minuscula (Codigo ASCII), corresponde a,", chr(numero))

# '''
# 2
# '''
# string=str(input("Ingresa un caracter: "))

# if len(string) == 1:
#     codigo= ord(string)
#     if (codigo % 2) == 0:
#         print(f"El caracter {string} en su codigo ASCII es par: {codigo}")
#     else:
#         print(f"El caracter {string} en su codigo ASCII es inpar: {codigo}")
# else:
#     print("Dato incorrecto, vuelva a intentarlo.")

# '''
# 3
# '''

# caracter = input("Ingrese un caracter: ")

# if caracter.isdigit():
#     print(f"El caracter {caracter} es un dígito")
# else:
#     print(f"El caracter {caracter} no es un dígito")

# '''
# 4
# '''
# def signo(h):
#     if h > 0:
#         print(f"El numero {h} es positivo ")
#     elif h == 0:
#         print(f"El numero {h} es 0 ")
#     else:
#         print(f"El numero {h} es negativo")

# h= float(input("Introduzca un numero, puede ser negativo o positivo: "))
# signo(h)

# '''
# 5
# '''
# import math

# def circulo():
#     centroX = float(input("Introduzca la coordenada en X del centro del circulo: "))
#     centroY = float(input("Introduzca la coordenada en Y del centro del circulo: "))
#     radio = float(input("Introduzca la longuitud del radio del circulo: "))
#     puntoX = float(input("Introduzca la coordenada en X del punto que quiere buscar: "))
#     puntoY = float(input("Introduzca la coordenada en X del punto que quiere buscar: "))
#     distancia = math.sqrt(((puntoX - centroX)**2)+((puntoY - centroY)**2))
#     if distancia > radio:
#         print(f"El punto ubicado en: {puntoX, puntoY}, no se encuentra en el circulo donde el centro se encuentra en las coordenadas {centroX, centroY} y con radio de {radio}")
#     elif distancia == radio:
#         print(f"El punto ubicado en: {puntoX, puntoY}, se encuentra en la circunferencia del circulo donde el centro se encuentra en las coordenadas {centroX, centroY} y con radio de {radio}")
#     else:
#         print(f"El punto ubicado en: {puntoX, puntoY}, se encuentra en el circulo donde el centro se encuentra en las coordenadas {centroX, centroY} y con radio de {radio}")

# circulo()

'''
6
'''
# def triangulo():
#     ladoA = float(input("Ingrese la longuitud del lado A: "))
#     ladoB = float(input("Ingrese la longuitud del lado B: "))
#     ladoC = float(input("Ingrese la longuitud del lado C: "))
#     if (ladoA + ladoB) > ladoC and (ladoC + ladoB) > ladoA and (ladoA + ladoC) > ladoB:
#         if ladoB == ladoA == ladoC:
#             print(f"El triangulo con lados de {ladoA, ladoB, ladoC} forma un triangulo equilatero")
#         elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
#             print(f"El triangulo con lados de {ladoA, ladoB, ladoC} forma un triangulo Isósceles")
#         else:
#             print(f"El triangulo con lados de {ladoA, ladoB, ladoC} forma un triangulo escaleno")
#     else:
#             print(f"No se puede formar un triangulo con lados: {ladoA, ladoB, ladoC}")

# triangulo()

'''
7
# '''
# import math

# def volumen(radio1, radio2, altura):
#     volumen_cono = ((math.pi*(radio2**2)*altura)/3)
#     volumen_esfera = ((4*math.pi*(radio1**3))/3)
#     return volumen_cono + volumen_esfera

# a = float(input("Ingrese el valor del radio de la esfera: "))
# b = float(input("Ingrese el valor del radio del cono: "))
# c = float(input("Ingrese el valor de la altura del cono: "))
# print(f"El volumen del solido presentado es de: {volumen(a,b,c)} u^3")

# print(volumen(3, 4, 9/2)) #La division es Exacta
# print(volumen(3, 4, 9//2)) # La division solo toma la parte entera
'''
8
'''
# from math import pi 

# def carrito():
#     altura = float(input("Ingrese el valor de la altura del rectangulo: "))
#     largo = float(input("Ingrese el valor del largo del rectangulo: "))
#     radio = float(input("Ingrese el valor del radio del circulo: "))
#     volumen_total = (altura*largo)+(pi*(radio**2))
#     print(f"El volumen total del vagon de largo {largo}, de altura {altura} y con ruedas de radio {radio} es: {round(volumen_total, 2)u^2}")

# carrito()

'''
9
'''
# from math import pi
# print(pi+pi+2)
# def iran():
#     radio1 = float(input("Ingrese el valor del radio de la rueda 1: "))
#     radio2 = float(input("Ingrese el valor del radio de la rueda 2: "))
#     largo1 =  float(input("Ingrese el valor del largo del rectangulo (B1): "))
#     altura1 = float(input("Ingrese el valor de la altura del rectangulo sobre las ruedas (A1): "))
#     largo2 =  float(input("Ingrese el valor del largo del rectangulo (B2): "))
#     altura2 = float(input("Ingrese el valor de la altura del rectangulo sobre el rectangulo (A2): "))
#     volumen_ruedas = pi * (radio1**2) + pi * (radio2**2)
#     volumen_bloque1 = largo1 * altura1
#     volumen_bloque2 = largo2 * altura2
#     volumen_Total = volumen_bloque1+ volumen_bloque2+volumen_ruedas
#     print(
#         f"El carro con ruedas de radio {radio1, radio2}, y los bloques sobre las ruedas de largo y altura: {(largo1, altura1), (largo2, altura2)}, \n tiene un area de: {volumen_Total} u^2"
#         )
    
# iran()

'''
10
'''

# def peso(N, M, K):
#     pesoN = 6*N
#     pesoM = 7*M
#     pesoK = 1*
#     total_Peso = pesoK + pesoM + pesoN
#     print(f"El peso total de las gallinas es: {pesoN}kg, el peso total de los gallos es de: {pesoM}kg,\n  el peso total de los pollitos es de: {pesoM}kg, el peso total es: {total_Peso}kg")
    
# n = int(input("Por favor, digite el numero de gallinas: "))
# m = int(input("Por favor, digite el numero de gallos: "))
# k = int(input("Por favor, digite el numero de pollitos: "))

# peso(n, m ,k)

'''
11
'''

# def vueltas():
#     panes = int(input("Por favor, Digite el numero de panes a comprar: "))
#     leche = int(input("Por favor, Digite el numero de bolsas de leche a comprar: "))
#     huevos = int(input("Por favor, Digite el numero de panes a comprar: "))
#     dinero = float(input("Por favor, Digite el dinero presupuestado: "))
#     panes_Total,leche_Total,huevos_Total = panes*300, leche*3300, huevos*350
#     vueltas = dinero - (panes_Total + huevos_Total + leche_Total)
#     if (vueltas >= 0):
#         print(f"El costo de los panes, huevos y leche es de: {panes_Total, huevos_Total, leche_Total} respectivamente y sobran: {vueltas}")
#     else:
#         print(f"El costo de los panes, huevos y leche es de: {panes_Total, huevos_Total, leche_Total} respectivamente y debe: {vueltas}")

# vueltas()

'''
12
'''

# def prestamo(interes, dinero, meses):
#     interes_c = interes/100
#     año = meses/12
#     cantidad = dinero*((1+interes_c)**año)
#     print(f"El valor a pagar del prestamo de {dinero}, con un interes de {interes}% con duracion de {meses} meses es de: {cantidad}")


# interes = float(input("Digite el porcentaje del interes: "))
# dinero = float(input("Digite la cantidad de  dinero: "))
# meses = float(input("Digite la cantidad de meses del prestamo: "))
# prestamo(interes, dinero, meses)

'''
13
'''

# def nuncaLandia():
#     contagiados = int(input("Digite el numero de contagiados el dia de hoy: "))
#     dias = int(input("Digite el numero de dias que van a transcurrir: "))
#     total = contagiados*(2**dias)
#     print(f"La cantidad de contagiados despues de {dias} es de: {contagiados*(2**dias)}")

# nuncaLandia()

'''
14
'''

def cantidad_Patas():
    cantidad = int(input("Coloque la cantidad en total de pollos y conejos: "))   
    patas = int(input("Digite la cantidad de patas que hay en el corral: "))
    pollo = abs((patas-(4*cantidad))/2)
    conejos = abs(cantidad-pollo)
    print("La cantidad de conejos y pollos son respectivamente:", conejos, pollo)

cantidad_Patas()