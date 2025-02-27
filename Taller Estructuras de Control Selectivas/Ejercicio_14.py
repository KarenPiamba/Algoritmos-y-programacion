#Entradas
lectura_anterior=int(input("Ingresa la lectura anterior del medidor (Kwh)"))
lectura_actual=int(input("Ingresa la lectura actual del medidor (Kwh)"))
#Caja negra
consumo=lectura_actual-lectura_anterior
if(0<=consumo<=100):
    print("El monto a pagar es:", (consumo*4600))
elif(101<=consumo<=300):
    print("El monto a pagar es:", (consumo*80000))
elif(301<=consumo<=500):
    print("El monto a pagar es:", (consumo*100000))
elif(consumo>=501):
    print("El monto a pagar es:", (consumo*120000))