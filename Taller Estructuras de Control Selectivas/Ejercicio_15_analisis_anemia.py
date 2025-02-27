"""
edad->int->edad
hemoglobina->float->hemoglobina
sexo->str->sexo
"""
#Entradas
edad=int(input("Ingresa tu edad en meses:"))
hemoglobina=float(input("Ingresa tu nivel de hemoglobina"))
sexo=input("Ingrese su sexo Femenino, Masculino (si tienes o eres menor 180 meses, escribir 0 en sexo):")
#Caja negra
if(edad>=0 and edad<=1 and hemoglobina<13 or hemoglobina>=26 and (sexo=="0")):
    print("positivo")
elif(edad<1 and edad<=6 and hemoglobina<10 or hemoglobina>=18 and (sexo=="0")):
    print("positivo")
elif(edad<6 and edad<=12 and hemoglobina<11 or hemoglobina>=15 and (sexo=="0")):
    print("positivo")
elif(edad<12 and edad<=60 and hemoglobina<11.5 or hemoglobina>=15 and (sexo=="0")):
    print("positivo")
elif(edad<60 and edad<=120 and hemoglobina<12.6 or hemoglobina>=15.5 and (sexo=="0")):
    print("positivo")
elif(edad<120 and edad<=180 and hemoglobina<13 or hemoglobina>=15.5 and (sexo=="0")):
    print("positivo")
elif(edad>180 and sexo=="Femenino" and hemoglobina<12 or hemoglobina>=16 ):
    print("positivo")
elif(edad>180 and sexo=="Masculino" and hemoglobina<12 or hemoglobina>=18):
    print("positivo")
else:
    print("Negativo")