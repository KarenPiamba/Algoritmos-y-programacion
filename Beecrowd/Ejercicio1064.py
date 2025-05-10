positivos = []
for i in range(6):
    numero = float(input())
    if numero > 0:
        positivos.append(numero)
cantidad_positivos = len(positivos)
promedio_positivos = sum(positivos) / cantidad_positivos
print(f"{cantidad_positivos} valores positivos")
print(f"{promedio_positivos:.1f}")