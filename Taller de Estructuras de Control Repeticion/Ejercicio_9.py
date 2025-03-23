nombres = []
puntajes = []
while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    puntaje = float(input("Ingrese el puntaje obtenido: "))
    
    nombres += [nombre]
    puntajes += [puntaje]
    
    if input("¿Desea ingresar otro estudiante? (Sí/No): ") not in ["Sí", "Si", "sí", "si"]:
        break
if puntajes:
    max_puntaje = max(puntajes)
    min_puntaje = min(puntajes)
    promedio = sum(puntajes) / len(puntajes)
    print("Resultados del análisis de puntajes:")
    print(f"Estudiante con el puntaje más alto: {nombres[puntajes.index(max_puntaje)]} ({max_puntaje})")
    print(f"Estudiante con el puntaje más bajo: {nombres[puntajes.index(min_puntaje)]} ({min_puntaje})")
    print(f"Promedio de todos los puntajes: {promedio:.2f}")
else:
    print("No se ingresaron datos.")