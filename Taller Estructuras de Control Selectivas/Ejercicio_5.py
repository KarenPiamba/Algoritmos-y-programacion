#Entradas
venta_departamento_1=int(input("Ingresa el importe de las ventas del departamento 1"))
venta_departamento_2=int(input("Ingresa el importe de las ventas del departamento 2"))
venta_departamento_3=int(input("Ingresa el importe de las ventas del departamento 3"))
salario=int(input("Ingresa tu salario mensual"))
#Caja negra
ventas_totales=venta_departamento_1+venta_departamento_2+venta_departamento_3
base_para_extras=ventas_totales*0.33
extras=salario*0.20
if(venta_departamento_1>=base_para_extras):
    print("Los vendedores del departamento 1 ganan:",salario+extras)
elif(venta_departamento_2>=base_para_extras):
    print("Los vendedores del departamento 2 ganan:",salario+extras)
elif(venta_departamento_3>=base_para_extras):
    print("Los vendedores del departamento 3 ganan:",salario+extras)
