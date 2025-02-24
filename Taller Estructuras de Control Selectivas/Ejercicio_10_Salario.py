#Entradas
Salario_bruto=int(input("Ingresa tu salario bruto"))
if(Salario_bruto==5000000):
    print("Su nuevo salario es:",((Salario_bruto*0.10)+Salario_bruto),"COP","Su categoria es 1")
elif(Salario_bruto==4300000):
    print("Su nuevo salario es:",((Salario_bruto*0.15)+Salario_bruto),"COP","Su categoria es 2")
elif(Salario_bruto==3600000):
    print("Su nuevo salario es:",((Salario_bruto*0.20)+Salario_bruto),"COP","Su categoria es 3")
elif(Salario_bruto==2000000):
    print("Su nuevo salario es:",((Salario_bruto*0.40)+Salario_bruto),"COP","Su categoria es 4")
elif(Salario_bruto==900000):
    print("Su nuevo salario es:",((Salario_bruto*0.60)+Salario_bruto),"COP","Su categoria es 5")
else:
    print("Po favor ingresa un valor valido")
    print("No corresponde a ninguna de las categorias")