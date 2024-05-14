import math #Importar libreria

#Funcion Cubo

def cubo ():
            lado = float(input("Escriba la longitud del lado: "))
            area_cubo, volumen_cubo = (6*(lado**2)), (lado**3) #Calcula Area Y Volumen
            print(#Resultado
                f"El área del cubo de lado {lado} es: {area_cubo}u^2\n El volumen del cubo de lado {lado} es: {volumen_cubo}u^3"
            )

#Funcion Esfera

def esfera ():
            radio = float(input("Escriba la longitud del radio: "))            
            area_esfera, volumen_esfera = math.prod([4, math.pi,(radio**2)]), (math.prod([(4/3),math.pi,(radio**3)]))  #Calcula Area y volumen
            print(f"El área de la esfera de radio {radio} es: {area_esfera} u^2\n El volumen del cubo de lado {radio} es: {volumen_esfera}u^3")

#Funcion Piramide

def piramide():
    cantidad = int(input("Cuantos lados tiene la base de la pirámide(tiene que ser mayor o igual a 3):"))
    lado = int(input("Cual es la longitud de los lados: "))
    if cantidad == 3:     #Calcula el area de la base a partir de la cantidad de lados y su longuitud
        raiz = (math.sqrt(3))
        area_base = math.prod([raiz, 0.25, (lado**2)])
    if cantidad == 4:
        area_base = lado ** 2
    if cantidad > 4:
        apotema = float(input("Cual es la longitud del apotema de la base(Si es decimal, use punto en vez de coma): "))
        perimetro = float(cantidad * lado)
        area_base = math.prod([perimetro, apotema])
        area_base = area_base/2
    elif cantidad < 3: #No hay bases de menos de 2 lados
        print("La cantidad de lados debe ser mayor o igual a 3")
        piramide()
    altura = float(input("Cual es la altura de la pirámide: ")) #Calcula area
    apotema_triangulo = float(input("Cual es el apotema de la pirámide: "))
    area_lateral = float(math.prod([cantidad, lado, apotema_triangulo]))
    area_lateral = (area_lateral)/2
    area, volumen_piramide = (area_base + area_lateral), math.prod([(1/3),area_base,altura]) #Calcula Volumen y Area
    print(
    f"El área de la pirámide con {cantidad} de lados, \n con longitud de {lado} es: {area}u^2\n El volumen de la pirámide con {altura} de altura es: {volumen_piramide}u^3"
    )


#Funcion Romboedro

def romboedro():
    diagonal_mayor = float(input("Cual es la diagonal mayor del romboedro: "))
    diagonal_menor = float(input("Cual es la diagonal menor del romboedro: "))
    area = math.prod([3,diagonal_mayor, diagonal_menor]) #Calcula area
    lado = float(input("Cual es la longitud de los lados: "))
    angulo = float(input("Cual es el ángulo entre sus lados lados: "))
    if angulo == 360:
        print("El angulo debe ser menor a 360")
        romboedro()
    coseno = (math.cos(math.radians(angulo))) #Calcula Volumen
    raiz = math.sqrt((1+(2*coseno)))
    volumen = math.prod([lado ** 3,(1-coseno), raiz])
    print( #Resultado
        f"El área del romboedro con su longitud de diagonal mayor y menor \n de {diagonal_mayor, diagonal_menor } es: {area}u^2 y su volumen es: {volumen}u^3"
    ) 

while True: #Bucle 

    #El usuario puede manejar cualquier funcion sin tener que iniciar siempre
        desicion = int(input( 
            "Añade un numero para la hallar el volumen y área que quiere realizar(1: cubo, 2: esfera, 3: Pirámide, 4: Romboedro, 5: Salir): "
        ))
        if desicion == 1:
            cubo() 
            pass
        if desicion == 2:
            esfera()
            pass
        if desicion == 3:
            piramide()
            pass
        if desicion == 4:
            romboedro()
            pass
        if desicion == 5:
            print("Creado por Ángel Suescun-asuescunr@unal.edu.co.")
            break
        elif desicion <= 0 or desicion >= 6:
            print("Opción incorrecta")
