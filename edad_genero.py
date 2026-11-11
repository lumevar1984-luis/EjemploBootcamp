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

if genero != "m" and genero != "h":
    print("El género ingresado no es válido ❌")
else:
    if edad >= 0 and edad <= 5:
        if genero == "m":
            grupo = " Es una Niña Pequeña 👶"
        else:
            grupo = "Es un Niño Pequeño 👶"

    elif edad >= 6 and edad <= 12:
        if genero == "m":
            grupo = "Es una Niña Grande 👧"
        else:
            grupo = "Es un Niño Grande 👦"

    elif edad >= 13 and edad <= 17:
        if genero == "m":
            grupo = "Es una Adolescente 👩"
        else:
            grupo = "Es un Adolescente 👨"

    elif edad >= 18 and edad <= 65:
        if genero == "m":
            grupo = "Es una Mujer Adulta 👩"
        else:
            grupo = "Es un Hombre Adulto 👨"

    elif edad >= 66 and edad <= 150:
        if genero == "m":
            grupo = "Es una Mujer Mayor 👵"
        else:
            grupo = "Es un Hombre Mayor 👴"

    else:
        grupo = "Edad no válida ❌"

    print(f"La edad ingresada es: {edad} años")
    print(f"Pertenece al grupo de: {grupo}")
    print(f"Fin del Programa")

