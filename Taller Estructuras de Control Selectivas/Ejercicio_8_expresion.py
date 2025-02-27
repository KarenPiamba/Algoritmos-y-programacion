#Entradas
P=int(input("Ingresa el valor de P"))
Q=int(input("Ingresa el valor de Q"))
#Caja negra
N=P**3+Q**4-2*P**2
if(N>680):
    print("P y Q satisfacen la exprecion:",N)
else:
    print("P y Q no satisfacen la exprecion:",N)