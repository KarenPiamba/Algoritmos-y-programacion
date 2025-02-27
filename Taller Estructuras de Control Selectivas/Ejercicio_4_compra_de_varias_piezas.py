Monto_compra=int(input("Ingresa el monto total de la compra"))
if(Monto_compra>5000000):
    invertir_empresa=Monto_compra*0.55
    prestamo_banco=Monto_compra*0.30
    credito_fabricante=Monto_compra-(invertir_empresa)-(prestamo_banco)
    interes=credito_fabricante*0
elif(Monto_compra<=5000000):
    invertir_empresa=Monto_compra*0.70
    credito_fabricante=Monto_compra*0.30
    interes=credito_fabricante*0.20
    prestamo_banco=Monto_compra*0
print("El monto a invertir en la empresa es:",invertir_empresa)
print("La cantidad prestada al banco es:",prestamo_banco)
print("La cantidad a pagar a crédito es:",credito_fabricante)
print("El monto a pagar por intereses es:",interes)