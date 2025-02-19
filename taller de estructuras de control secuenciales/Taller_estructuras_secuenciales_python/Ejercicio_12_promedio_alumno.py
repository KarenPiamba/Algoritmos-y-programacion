#Entradas
Nota_examen_matematicas=int(input("Nota del examen de matematicas"))
Nota_examen_fisica=int(input("Nota del examen de fisica"))
Nota_examen_quimica=int(input("Nota del examen de quimica"))
Nota_tarea_1_matematicas=int(input("Nota 1 de la tarea de matematicas"))
Nota_tarea_2_matematicas=int(input("Nota 2 de la tarea de matematicas"))
Nota_tarea_3_matematicas=int(input("Nota 3 de la tarea de matematicas"))
Nota_tarea_1_fisica=int(input("Nota 1 de la tarea de fisica"))
Nota_tarea_2_fisica=int(input("Nota 2 de la tarea de fisica"))
Nota_tarea_1_quimica=int(input("Nota 1 de la tarea de quimica"))
Nota_tarea_2_quimica=int(input("Nota 2 de la tarea de quimica"))
Nota_tarea_3_quimica=int(input("Nota 3 de la tarea de quimica"))
#Caja negra
Promedio_tarea_matematicas=((Nota_tarea_1_matematicas+Nota_tarea_2_matematicas+Nota_tarea_3_matematicas)/3)*0.1
Promedio_tarea_fisica=((Nota_tarea_1_fisica+Nota_tarea_2_fisica)/2)*0.2
Promedio_tarea_quimica=((Nota_tarea_1_quimica+Nota_tarea_2_quimica+Nota_tarea_3_quimica)/3)*0.15
Promedio_examen_matematicas=Nota_examen_matematicas*0.9
Promedio_examen_fisica=Nota_examen_fisica*0.8
Promedio_examen_quimica=Nota_examen_quimica*0.85
Promedio_total_matematicas=Promedio_tarea_matematicas+Promedio_examen_matematicas
Promedio_total_fisica=Promedio_tarea_fisica+Promedio_examen_fisica
Promedio_total_quimica=Promedio_tarea_quimica+Promedio_examen_quimica
Promedio_general=(Promedio_total_quimica+Promedio_total_fisica+Promedio_total_matematicas)/3
#Salidas
print("El promedio en matematicas fue de:", Promedio_total_matematicas,"El promedio en fisica fue de:", Promedio_total_fisica,"El promedio en quimica fue de:", Promedio_total_quimica,"Su promedio general en las tres materias fue de:", Promedio_general)