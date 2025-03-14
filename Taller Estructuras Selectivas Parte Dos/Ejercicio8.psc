Algoritmo Ejercicio8
	Escribir "Escribe tu calificacion"
	Leer calificacion
	Si calificacion<90 Entonces
		Si calificacion>=80 y calificacion<90 Entonces
			Escribir "B"
		SiNo
			Si calificacion>=70 y calificacion<80 Entonces
				Escribir "C"
			SiNo
				Si calificacion>=60 y calificacion<70 Entonces
					Escribir "D"
				SiNo
					Escribir "F"
				Fin Si
			Fin Si
		Fin Si
	SiNo
		Escribir "A"
	Fin Si
FinAlgoritmo
