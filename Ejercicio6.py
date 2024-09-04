# Leer los tres números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

# Comparar y ordenar los números
if (numero1 <= numero2) and (numero1 <= numero3):
    if numero2 <= numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1, numero3, numero2)
elif (numero2 <= numero1) and (numero2 <= numero3):
    if numero1 <= numero3:
        print(numero2, numero1, numero3)
    else:
        print(numero2, numero3, numero1)
else:
    if numero1 <= numero2:
        print(numero3, numero1, numero2)
    else:
        print(numero3, numero2, numero1)
