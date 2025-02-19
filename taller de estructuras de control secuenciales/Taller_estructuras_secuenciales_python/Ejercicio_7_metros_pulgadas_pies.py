#Entradas
metros=int(input("Ingresa la cantidad de metros:"))
#Caja negra
Pulgadas=metros*39.27
Pies=Pulgadas/12
Pulgadas_restantes=Pulgadas%12
#Salida
print("De metros a pulgadas el valor es:",Pulgadas,"pies","De pulgadas a pie el valor es",Pies,"pies","Restante al convertir de pulgadas a pie",Pulgadas_restantes,"pulgadas")