n = int(input("Ingrese el número de estudiantes: "))
max_altura = 0
for estudiante in range(n):
    altura = float(input(f"Ingrese la altura del estudiante {estudiante + 1}: "))
    if altura > max_altura:
        max_altura = altura
print(f"La mayor altura registrada es: {max_altura}")
