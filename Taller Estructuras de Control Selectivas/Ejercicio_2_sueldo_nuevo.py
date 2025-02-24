#Entradas
Sueldo_del_trabajador=int(input("Ingresa el sueldo del trabajador"))
if(Sueldo_del_trabajador<900000):
    print("El nuevo sueldo deñ trabajador es:",((Sueldo_del_trabajador*0.15)+Sueldo_del_trabajador),"COP")
elif(Sueldo_del_trabajador>900000):
    print("El nuevo sueldo deñ trabajador es:",((Sueldo_del_trabajador*0.12)+Sueldo_del_trabajador),"COP")
else(900000==900000):
    print("No aplica")