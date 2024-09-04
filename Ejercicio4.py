# Pide al usuario que introduzca el primer número
A = int(input("Introduce el primer número entero positivo A: "))

# Pide al usuario que introduzca el segundo número
B = int(input("Introduce el segundo número entero positivo B: "))

# Verifica si A y B son números enteros positivos
if A > 0 and B > 0:
    # Comprueba si A es múltiplo de B
    if A % B == 0:
        print(f"{A} es múltiplo de {B}.")
    else:
        print(f"{A} no es múltiplo de {B}.")
else:
    # Mensaje de error si alguno de los números no es positivo
    print("Error: Ambos números deben ser enteros positivos.")
