# Edad de una persona
# 0 a 5 años: Grupo de niños pequeños
# 6 a 12 años: Grupo de niños grandes
# 13 a 17 años: Grupo de Adolescentes   
# 18 a 65 años: Grupo de Adultos
# 66 a 100 años: Grupo de Adultos Mayores

edad_persona = int(input("Ingrese la edad de la persona: "))

if edad_persona >= 0 and edad_persona <= 5:
    grupo = "Niño Pequeño"

elif edad_persona >= 6 and edad_persona <= 12:
    grupo = "Niño Grande"

elif edad_persona >= 13 and edad_persona <= 17:
    grupo = "Adolescente"

elif edad_persona >= 18 and edad_persona <= 65:
    grupo = "Adulto"

elif edad_persona >= 66 and edad_persona <= 150:
    grupo = "Adulto Mayor"

else:
    grupo = "Edad no válida"

grupo = "Niño Pequeño" if edad_persona >= 0 and edad_persona <= 5 else \
        "Niño Grande" if edad_persona >= 6 and edad_persona <= 12 else \
        "Adolescente" if edad_persona >= 13 and edad_persona <= 17 else \
        "Adulto" if edad_persona >= 18 and edad_persona <= 65 else \
        "Adulto Mayor" if edad_persona >= 66 and edad_persona <= 150 else "Edad no válida"


print(f"La edad ingresada es: {edad_persona} años")
print(f"Pertenece al grupo de: {grupo}")
print(f"Fin del Programa")