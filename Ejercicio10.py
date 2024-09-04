edad = int (input("Ingrese su edad: "))
if edad >= 0 and edad<= 12:
        print ("Niño")
elif edad>= 12 and edad<=17:
        print ("Adolescente")
elif edad>= 18 and edad < 24:
        print ("Adulto")        
elif edad>= 24 and edad < 60:
        print ("Adulto")
elif edad>= 60:
        print ("Adulto mayor")
else:
        print ("Edad fuera de rango")