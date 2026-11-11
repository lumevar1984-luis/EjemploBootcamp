# Edad de una persona
# 0 a 5 años: Grupo de niños pequeños
# 6 a 12 años: Grupo de niños grandes
# 13 a 17 años: Grupo de Adolescentes   
# 18 a 65 años: Grupo de Adultos
# 66 a 100 años: Grupo de Adultos Mayores


edad = int(input("Ingrese la edad: "))
# lower() convierte a minúscula el valor ingresado
# upper() convierte a mayúscula el valor ingresado
genero = input("Ingrese el género 'm' o 'h' en caso de ser mujer o hombre: ").lower()

if edad >= 0 and edad <= 5:
    if genero == "m":
        grupo = "Niña Pequeña"
    else:
        grupo = "Niño Pequeño"

elif edad >= 6 and edad <= 12:
    if genero == "m":
        grupo = "Niña Grande"
    else:
        grupo = "Niño Grande"

elif edad >= 13 and edad <= 17:
    if genero == "m":
        grupo = "Chica Adolescente"
    else:
        grupo = "Chico Adolescente"

elif edad >= 18 and edad <= 65:
    if genero == "m":
        grupo = "Mujer Adulta"
    else:
        grupo = "Hombre Adulto"

elif edad >= 66 and edad <= 150:
    if genero == "m":
        grupo = "Mujer Mayor"
    else:
        grupo = "Hombre Mayor"

else:
        grupo = "Edad no válida"

print(f"La edad ingresada es: {edad} años")
print(f"Pertenece al grupo de: {grupo}")
print(f"Fin del Programa")

