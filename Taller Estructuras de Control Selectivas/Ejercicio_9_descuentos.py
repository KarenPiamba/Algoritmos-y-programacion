#Entradas
monto_compra=int(input("Ingresa el monto de la compra"))
#Caja negra
if(monto_compra<=50000):
    print("No hay descuento")
elif(50000<monto_compra<=100000):
    N=monto_compra*0.05
    Valor_nuevo=monto_compra-N
    print("El descuento es de:", N, "El valor totala pagar con el descuento es de:",Valor_nuevo)
elif(100000<monto_compra<=700000):
    N=monto_compra*0.11
    Valor_nuevo=monto_compra-N
    print("El descuento es de:", N, "El valor totala pagar con el descuento es de:",Valor_nuevo)
elif(700000<monto_compra<=1500000):
    N=monto_compra*0.18
    Valor_nuevo=monto_compra-N
    print("El descuento es de:", N, "El valor totala pagar con el descuento es de:",Valor_nuevo)
elif(monto_compra<1500000):
    N=monto_compra*0.25
    Valor_nuevo=monto_compra-N
    print("El descuento es de:", N, "El valor totala pagar con el descuento es de:",Valor_nuevo)