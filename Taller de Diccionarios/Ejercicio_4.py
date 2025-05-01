estudiantes = {
    "1": {
        "nombre": "Lorea",
        "nota": 8
    },
    "2": {
        "nombre": "Markel",
        "nota": 4.2
    },
    "3": {
        "nombre": "Julen",
        "nota": 6.5
    }
}
max_estudiantes = 10
estudiantes_actuales = len(estudiantes)
estudiantes_por_agregar = max_estudiantes - estudiantes_actuales
for i in range(estudiantes_actuales + 1, max_estudiantes + 1):
    nombre = input(f"Introduce el nombre del estudiante {i}: ")
    while True:
        try:
            nota = float(input(f"Introduce la nota de {nombre}: "))
            break 
        except ValueError:
            print("Por favor, introduce una nota válida (número).")
    estudiantes[str(i)] = {
        "nombre": nombre,
        "nota": nota
    }
aprobados = []
suspendidos = []
total_notas = 0
for estudiante in estudiantes.values():
    total_notas=total_notas+estudiante["nota"]
    if estudiante["nota"] >= 5:
        aprobados.append(estudiante["nombre"])
    else:
        suspendidos.append(estudiante["nombre"])
nota_media = total_notas / len(estudiantes)
print("Estudiantes aprobados:", aprobados)
print("Estudiantes suspendidos:", suspendidos)
print(f"Nota media de la clase: {nota_media}")
