suma = 0
k=1
while True:
    termino=(k**2 + 1) / k 
    if suma+termino > 1000:
        break
    suma=suma+termino 
    print(f"Término {k}: {termino:.4f}, Suma acumulada: {suma:.4f}")
    k=k+1 
print(f"Número total de términos sumados: {k-1}")
print(f"Suma acumulada: {suma:.4f}")