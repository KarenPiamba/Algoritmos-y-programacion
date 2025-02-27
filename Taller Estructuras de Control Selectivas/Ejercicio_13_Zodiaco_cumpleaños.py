#Entradas
dia=int(input("Ingresa el dia en que naciste (1-31)"))
mes=int(input("Ingresa el mes en que naciste (1-12)"))
año=int(input("Ingresa el año en que naciste"))
dia_actual=int(input("Ingresa el dia de hoy (1-31)"))
mes_actual=int(input("Ingresa el mes de actual (1-12)"))
año_actual=int(input("Ingresa el año de actual"))
#Caja negra
Edad=(año_actual-año)
if((mes_actual>mes) or (mes_actual==mes and dia_actual>dia)):
    print("Tu edad es:", Edad)
No_has_cumplido_años=(Edad-1)
if((mes_actual<mes) or (mes_actual==mes and dia_actual<dia)):
    print("Tu edad es:", No_has_cumplido_años)
elif((mes==11 and dia>=22) or (mes==12 and dia<=21)):
    print("Tu signo zodiacal es Sagitario")
elif((mes==12 and dia>=22) or (mes==1 and dia<=20)):
    print("Tu signo zodiacal es Capricornio")
elif((mes==1 and dia>=21) or (mes==2 and dia<=19)):
    print("Tu signo zodiacal es Acuario")
elif((mes==2 and dia>=20) or (mes==3 and dia<=19)):
    print("Tu signo zodiacal es Picis")
elif((mes==3 and dia>=20) or (mes==4 and dia<=20)):
    print("Tu signo zodiacal es Aries")
elif((mes==4 and dia>=21) or (mes==5 and dia<=21)):
    print("Tu signo zodiacal es Tauro")
elif((mes==5 and dia>=22) or (mes==6 and dia<=21)):
    print("Tu signo zodiacal es Geminis")
elif((mes==6 and dia>=22) or (mes==7 and dia<=22)):
    print("Tu signo zodiacal es Cancer")
elif((mes==7 and dia>=23) or (mes==8 and dia<=23)):
    print("Tu signo zodiacal es Leo")
elif((mes==8 and dia>=24) or (mes==9 and dia<=22)):
    print("Tu signo zodiacal es Virgo")
elif((mes==9 and dia>=23) or (mes==10 and dia<=22)):
    print("Tu signo zodiacal es Libra")
elif((mes==10 and dia>=23) or (mes==11 and dia<=21)):
    print("Tu signo zodiacal es Escorpion")