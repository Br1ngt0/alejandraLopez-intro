# Entrada: horas y minutos de estacionamiento
horas = int(input("Ingrese las horas de estacionamiento: "))
minutos = int(input("Ingrese los minutos de estacionamiento: "))

# Tarifa por hora
tarifa_por_hora = 1.500

# Cálculo del tiempo total en horas
if minutos > 0:
    # Si hay minutos adicionales, se cobra una hora completa
    horas_totales = horas + 1
else:
    horas_totales = horas

# Cálculo del monto a pagar
monto_a_pagar = horas_totales * tarifa_por_hora

# Salida: monto a pagar
print("El monto a pagar por el estacionamiento es: $/.", monto_a_pagar)
