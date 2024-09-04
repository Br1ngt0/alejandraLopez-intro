# Algoritmo para calcular el día siguiente de una fecha

# Leer datos de entrada: día, mes, año
día = int(input("Introduce el día (1...31): "))
mes = int(input("Introduce el mes (1...12): "))
año = int(input("Introduce el año: "))

# Definir el número de días en cada mes
if mes in [1, 3, 5, 7, 8, 10, 12]: 
    días_en_mes = 31
elif mes in [4, 6, 9, 11]: 
    días_en_mes = 30
elif mes == 2: 
    días_en_mes = 28

# Verificar si es el último día del mes
if día < días_en_mes: 
    día += 1
else:
    día = 1
    # Verificar si es el último mes del año
    if mes == 12:
        mes = 1
        año += 1
    else:
        mes += 1

# Mostrar la fecha del día siguiente
print("La fecha del día siguiente es:", día, "/", mes, "/", año)
