#Entrada
Calificacion_parcial_1=float(input("Ingresa la calificacion parcial 1"))
Calificacion_parcial_2=float(input("Ingresa la calificacion parcial 2"))
Calificacion_parcial_3=float(input("Ingresa la calificacion parcial 3"))
Examen_final=float(input("Ingresa la calificacion del examen final"))
Trabajo_final=float(input("Ingresa la calificacion del trabajo final"))
#Caja negra
Promedio_parciales=((Calificacion_parcial_1+Calificacion_parcial_2+Calificacion_parcial_3)/3)*0.55
Examen=(Examen_final*0.30)
Trabajo=(Trabajo_final*0.15)
#Salida
print("La calificacion final es:", Promedio_parciales+Examen+Trabajo)