#Entradas
A=int(input("Ingresa el valor de A (0-9)"))
B=int(input("Ingresa el valor de B (0-9)"))
C=int(input("Ingresa el valor de C (0-9)"))
D=int(input("Ingresa el valor de D (0-9)"))
#CAJA NEGRA
K=((A*1000+B*100+C*10+D))
if(C>=5):
    N=((A*1000+(B+1)*100+C*0+D*0))
elif(C<5):
    N=((A*1000+B*100+C*0+D*0))
#SALIDA
print("El resultado sin redondear es:",K)
print("El resultado redondeado es:",N)