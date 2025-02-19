#Entradas
Nombre=input("Nombre del trabajador")
Numero_de_horas_normalmente_trabajadas=int(input("Numero de horas normalmente trabajadas"))
Pago_de_una_hora_normal=int(input("Pago de una hora normal"))
Numero_de_horas_extras_trabajadas=int(input("Numero de horas extras trabajadas"))
Actualizacion_academica=int(input("Numero de actualizaciones academicas"))
Numero_de_hijos=int(input("Numero de hijos"))
#Caja negra
Valor_horas_extras=Numero_de_horas_extras_trabajadas*0.25
Total_deducido=Pago_de_una_hora_normal+Valor_horas_extras
Pago_forzoso=Total_deducido*0.05
Politica_habitaciones=Total_deducido*0.02
Caja_de_ahorro=Total_deducido*0.07
Valor_por_actualizacion_academica_total=Actualizacion_academica*250000
Valor_por_numero_de_hijos_total=Numero_de_hijos*173000
Prima_por_hogar=180000
Total_deducciones=Pago_forzoso+Politica_habitaciones+Caja_de_ahorro
Asignaciones=Prima_por_hogar+Valor_por_numero_de_hijos_total+Valor_por_actualizacion_academica_total
Sueldo_neto=Total_deducido+Asignaciones-Total_deducciones
#Salidas
print("Tu sueldo para diciembre es de:", Sueldo_neto,"COP", "Tus deducciones fueron:",Total_deducciones,"COP","Tus asignaciones fueron:",Asignaciones,"COP")