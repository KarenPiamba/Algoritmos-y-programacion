#ejercicio 6
dividendo=int(input("ingrese el numero dividendo: "))
divisor=int(input("ingrese el divisor: "))
contador=0
residuo = dividendo
while residuo >= divisor:
        residuo = residuo - divisor
        contador = contador+1
print(f"Cociente: {contador}")
print(f"Residuo: {residuo}")