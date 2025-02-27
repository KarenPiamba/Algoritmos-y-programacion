# Entradas
cantidad_ingresada = int(input("Ingresa la cantidad en COP: "))
# Caja negra
billetes = (100000, 50000, 20000, 10000, 5000, 2000, 1000)
monedas = (500, 200, 100, 50)
cantidad = cantidad_ingresada - (cantidad_ingresada % 50)
resultado = []
for valor in billetes + monedas:
    if cantidad >= valor:
        cantidad_billetes = cantidad//valor
        cantidad -= cantidad_billetes * valor
        resultado.append(str(valor))
if resultado:
    print(",".join(resultado))
else:
    print("No hay billetes o monedas disponibles para esta cantidad.")
