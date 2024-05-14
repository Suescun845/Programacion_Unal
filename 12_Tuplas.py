tupla = (23, "Hola un", "R")
print("Mi tupla: ", tupla)
tupla2 = (4.5, "Ingenieria", 60, True, "Y", ("Lunes", 6))
print("Mi tupla: ", tupla2)
tupla3 = ("Un solo elemnto")
print("Mi tupla: ", tupla3)
tupla4 = ("Hola", True, "Systems")
a, b, c = tupla4
print("Mi valor a: ", a)
print("Mi valor b: ", b)
print("Mi valor c: ", c)
tupla5 = (tupla, tupla2)
print("Mi tupla: ", tupla5)
print("Mi tupla: ", tupla5[1])
print("Mi tupla: ", tupla5[0][1])
print("Mi tupla: ", tupla2[-1])
text = "Cien Años De Soledad"

if ("años" in text):
    print("Si esta en la tupla")
else:
    print("No esta en la tupla")

for palabra in text:
    print(palabra, end=",")



