numero= int(input("Ingrese un número entero positivo: "))
suma = 0
print(f"Divisores propios de {numero}:", end="")
for i in range(1, numero):
    if numero % i == 0:
        print(f"+{i}", end=" ")  # Imprimir el divisor
        suma += i
print()  # Salto de línea
if suma == numero:
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
