lista1 = ["Hello", "World", 12, True]
lista2 = ["Hola", "Mundo", False, [ "Profe", "Hay","Mejores",12345, 13.56543], "Pinguino", (33, 45,34, "Soy una querida tupla <3")]
print(lista2)
lista3 = lista2 [3][0] #Ubicacion de un objeto que queramos pasar a otra variable
print(lista3)
print(lista2 [3][2])
print(lista2[2:4:]) #Rango de lista
lista2.append("Frailejon Ernesto Perez")
print(lista2)
names = ["Felipe", "Ernesto", "Pico", "adfghjhgf","Pto"]
names.sort() #Organiza de menor a mayor, con true al revez
print(names)
names.sort(reverse=True)
print(names)
names.append("Pico") #Agrega valores a la lista
print(names)
names.remove("Pico") #elimina valores a la lista
print(names)
names.pop(3) # Elimina con posicion
print(names)
### Diccionarios ###

dict1 = {"key": "Valor", 
        5:345.5, 
        "t":True, 
        "List": names
        }
