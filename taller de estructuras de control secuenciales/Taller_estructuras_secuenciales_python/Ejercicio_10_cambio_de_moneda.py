#Entrada
Cantidad_de_chelines_austriacos=int(input("Numero de chelines austriacos"))
Cantidad_de_dracmas_griegos=int(input("Numero de dracmas griegos"))
Cantidad_de_pesetas=int(input("Numero de pesetas"))
#Caja negra
Pesetas=(Cantidad_de_chelines_austriacos*956871)/100
Francos_franceses_parte_1=(Cantidad_de_dracmas_griegos*88607)/100
Francos_franceses=Francos_franceses_parte_1/20110
Dolar=Cantidad_de_pesetas/122499
Liras_italianas=100/Cantidad_de_pesetas
#Salida
print("De chelines austruacos a pesetas:", Pesetas,",","De dracmas griegros a francos franceses:",Francos_franceses,",","De pesetas a dolar:",Dolar,",","De pesetas a liras italianas:",Liras_italianas)