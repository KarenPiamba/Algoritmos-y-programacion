#Entradas
mujeres=int(input("Ingrese cantidad de mujeres:"))
hombres=int(input("Ingrese cantidad de hombres:"))
#Caja negra
total_estudiantes=mujeres+hombres
porcentaje_mujeres=(mujeres/total_estudiantes)*100
porcentaje_hombres=(hombres/total_estudiantes)*100
#Salida
print("El porcentaje de mujeres: ",porcentaje_mujeres,"%","porcentaje de hombres: ",porcentaje_hombres,"%")