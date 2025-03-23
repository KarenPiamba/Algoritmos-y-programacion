total_encuestados = 0
conteo_licor = 0
preferencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
suma_edades_cerveza = 0
conteo_cerveza = 0
mujeres_menores = 0
hombres_sin_aguardiente = 0
hombres = 0
mujeres = 0
while True:
    total_encuestados=total_encuestados+1
    print(f"Encuestado {total_encuestados}:")
    consume = input("¿Consume licor? (Sí/No): ")
    if consume in ["Sí", "sí", "Si", "si"]:
        conteo_licor=conteo_licor+1
        licor = int(input("Elija su licor preferido (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))
        if licor in preferencias:
            preferencias[licor]=preferencias[licor]+1
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo (M/F): ")
    if sexo in ["M", "m"]:
        hombres=hombres+1
        if edad >= 20 and edad <= 25 and (1 not in preferencias or preferencias[1] == 0):
            hombres_sin_aguardiente=hombres_sin_aguardiente+1
    else:
        mujeres=mujeres+1
        if edad < 18:
            mujeres_menores=mujeres_menores+1
    if consume in ["Sí", "sí", "Si", "si"] and licor == 3:
        suma_edades_cerveza=suma_edades_cerveza+edad
        conteo_cerveza=conteo_cerveza+1
    continuar = input("¿Desea continuar con la encuesta? (Sí/No): ")
    if continuar not in ["Sí", "sí", "Si", "si"]:
        break
promedio_edad_cerveza = suma_edades_cerveza / conteo_cerveza if conteo_cerveza > 0 else 0
porcentaje_whisky = (preferencias[5] / total_encuestados) * 100 if total_encuestados > 0 else 0
licor_mas_preferido = max(preferencias, key=lambda x: preferencias[x])
print("\nResultados de la encuesta:")
print(f"Total de personas que consumen licor: {conteo_licor}")
print(f"Total de mujeres menores de edad: {mujeres_menores}")
print(f"Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años: {hombres_sin_aguardiente}")
print(f"Promedio de edad de quienes consumen cerveza: {promedio_edad_cerveza:.2f}")
print(f"Porcentaje de personas que consumen whisky respecto al total encuestado: {porcentaje_whisky:.2f}%")