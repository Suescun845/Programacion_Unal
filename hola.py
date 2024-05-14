a = int(input("Dame un numero"))
b = int(input("Dame otro numero"))
c = int(input("Dame otro numero"))

if a > b:
    if a > c:
        if b > c:
            mayor = a
            medio = b
            menor = c
        else:
            mayor = a
            medio = c
            menor = b    
    else:
        mayor = c
        medio = a
        menor = b
elif b > c:
    if a > c:
        mayor = b
        medio = a
        menor = c
    else:
        mayor = b
        medio = c
        menor = a
else:
    mayor = c
    medio = b
    menor = a

print(f"El mayor es {mayor}, el mediano es {medio} y el menor es {menor}")