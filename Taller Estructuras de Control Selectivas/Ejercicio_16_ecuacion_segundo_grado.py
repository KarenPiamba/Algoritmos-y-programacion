import math
# Entradas
a=int(input("Ingresa el coeficiente de a"))
b=int(input("Ingresa el coeficiente de b"))
c=int(input("Ingresa el coeficiente de c"))
#Caja negra
d=b**2-4*a*c
if(d==0):
    x=-b/(2*a)
    print("el valor de x es:",x)
elif(d>0):
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print(f"las soluciones son: x1={x1},x2={x2}")
else:
    print("no tiene solucion entre los numeros reales")