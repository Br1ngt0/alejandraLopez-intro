Algoritmo OrdenarTresNumeros
		Definir numero1, numero2, numero3 Como Real
		Escribir "Ingresa el primer número: "
		Leer numero1
		Escribir "Ingresa el segundo número: "
		Leer numero2
		Escribir "Ingresa el tercer número: "
		Leer numero3
		
		
		Si (numero1 <= numero2) Y (numero1 <= numero3) Entonces
			Si (numero2 <= numero3) Entonces
				Escribir numero1, ", ", numero2, ", ", numero3
			SiNo
				Escribir numero1, ", ", numero3, ", ", numero2
			FinSi
		Sino
			Si (numero2 <= numero1) Y (numero2 <= numero3) Entonces
				Si (numero1 <= numero3) Entonces
					Escribir numero2, ", ", numero1, ", ", numero3
				SiNo
					Escribir numero2, ", ", numero3, ", ", numero1
				FinSi
			Sino
				Si (numero1 <= numero2) Entonces
					Escribir numero3, ", ", numero1, ", ", numero2
				SiNo
					Escribir numero3, ", ", numero2, ", ", numero1
				FinSi
			FinSi
		FinSi
FinAlgoritmo
