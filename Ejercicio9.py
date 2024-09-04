# Algoritmo para calcular el tiempo transcurrido entre dos horas H-1 y H-2
# Se ingresan las horas y minutos de H-1 y H-2 desde el teclado

# 1. Ingresar las horas y minutos de H-1
hora_1 = int(input("Ingrese la hora de H-1 (0-23): "))
minutos_1 = int(input("Ingrese los minutos de H-1 (0-59): "))

# 2. Ingresar las horas y minutos de H-2
hora_2 = int(input("Ingrese la hora de H-2 (0-23): "))
minutos_2 = int(input("Ingrese los minutos de H-2 (0-59): "))

# 3. Calcular la diferencia en horas y minutos entre H-1 y H-2
# Calcular minutos totales para H-1 y H-2
minutos_totales_H1 = hora_1 * 60 + minutos_1
minutos_totales_H2 = hora_2 * 60 + minutos_2

# 4. Calcular la diferencia entre los tiempos
diferencia_minutos = minutos_totales_H2 - minutos_totales_H1

# 5. Si la diferencia es negativa, se toma el valor absoluto
if diferencia_minutos < 0:
    diferencia_minutos = abs(diferencia_minutos)

# 6. Convertir la diferencia en horas y minutos
diferencia_horas = diferencia_minutos // 60
diferencia_minutos_restantes = diferencia_minutos % 60

# 7. Mostrar el tiempo transcurrido
print("El tiempo transcurrido es de:", diferencia_horas, "horas y", diferencia_minutos_restantes, "minutos")
