#Entradas
A=int(input("Ingresa el valor de la inversion"))
B=float(input("Tasa de interes en decimal"))
#Caja negra
C=A*B
if(C>100000):
    print("Los intereses exceden los 100.000 COP, Se reinvertiran")
elif(C<=100000):
    print("Los intereses no exceden los 100.000 COP, No se reinvertiran")