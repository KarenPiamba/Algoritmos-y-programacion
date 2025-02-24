#Entradas
Dato_A=int(input("Ingresa el valor A"))
Dato_B=int(input("Ingresa el valor B"))
Dato_C=int(input("Ingresa el valor C"))
Dato_D=int(input("Ingresa el valor D"))
#Caja negra y salida
if(Dato_D==0):
    print((Dato_A-Dato_C)**2)
elif(Dato_D>0):
    print(((Dato_A-Dato_B)**3)/Dato_D)
