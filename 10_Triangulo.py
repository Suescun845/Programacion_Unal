### Tipo de Triangulo ###

print(
    "Este programa comprueba si se puede formar un triángulo y que tipo de triangulo se forma. "
        )
a = int(input("Coloque la longuitud del lado a: "))
b = int(input("Coloque la longuitud del lado b: "))
c = int(input("Coloque la longuitud del lado c: "))
if a + b > c and c + b > a and c + a > a:
    if a == b and a == c:
        print(f"Se puede formar un triángulo equilátero con lados: {a, b, c}")
    elif a== c or b ==c or b == a:
        print(f"Se puede formar un triángulo isósceles con lados: {a, b, c}")
    else:
        print(f"Se puede formar un triángulo escaleno con lados: {a, b, c}")
else:
    print(f"No se puede formar un triangulo con lados: {a,b,c}")

"""
Hecho Por Angel Suescun
"""