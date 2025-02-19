#Entradas
Precio_de_hora=int(input("Ingrese el valor por hora trabajada:"))
Horas_trabajadas=int(input("Ingrese la cantidad de horas trabajada:"))
#Caja negra
Salario_base=Precio_de_hora*Horas_trabajadas
Descuento_fijo=Salario_base*0.20
Salario_neto=(Salario_base-Descuento_fijo)
#Salida
print("El salario neto es:",Salario_neto)