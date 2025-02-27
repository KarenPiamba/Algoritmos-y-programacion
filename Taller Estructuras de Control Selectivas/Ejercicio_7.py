#Entradas
distancia_recorrda=int(input("Ingresa la distancia recorrida en km"))
#Caja negra
if(0<=distancia_recorrda<=300):
    print("Debes pagar:50000")
elif(1000>=distancia_recorrda>300):
    N=(distancia_recorrda-300)*30000
    P=N+70000
    print("Debes pagar:",P)
elif(distancia_recorrda>1000):
    N=(distancia_recorrda-300)*9000
    P=N+150000
    print("Debes pagar:",P)
else:
    print("Error")