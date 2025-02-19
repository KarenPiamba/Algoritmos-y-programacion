import math
# Entradas
Lado_1 = int(input("Ingresa el valor del lado 1: "))
Lado_2 = int(input("Ingresa el valor del lado 2: "))
Lado_3 = int(input("Ingresa el valor del lado 3: "))
# Caja negra
semiperimetro = (Lado_1 + Lado_2 + Lado_3) / 2 
Area = math.sqrt(semiperimetro * (semiperimetro - Lado_1) * (semiperimetro - Lado_2) * (semiperimetro - Lado_3))
# Salida
print("El área del triángulo es:", Area)