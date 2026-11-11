# True
# False

# x=True

# m=10
# n=5
# r=2
# p=12

# if m > n and p < r: # True
#     print("verdadero")
# else:
#     print("Falso")
# pass

# if m > n or p < r: # True
#     print("Verdadero")
# else:
#     print("Falso")
# pass

# if (m<p>r) and (m<p or m>p+3) and (m<p or n>p):
#     print("Verdadero")
# else:
#     print("Falso")
# pass

# usuario = input("Ingrese su usuario: ")
# clave = input("Ingrese su clave: ")

# if usuario == "lucas" and clave == "123":
#     print("Bienvenido al Sistema")
# else:
#     print("Usuario o Clave incorrectos")

# En una institución educativa se realizará un torneo académico exclusivo para estudiantes que cumplan ciertos requisitos. Para poder participar, el estudiante debe tener una nota promedio igual o superior a 4.0 y una asistencia mínima del 85%. Sin embargo, existe una excepción: si el estudiante ha ganado algún reconocimiento académico durante el año, puede participar aunque no cumpla uno de los dos requisitos anteriores. El sistema debe evaluar si el estudiante puede participar o no en el torneo según esta información. Se deben pedir los datos necesarios y mostrar un mensaje claro indicando si puede o no participar.

# nota_promedio >= 4
# asistencia >= 85%

# nota_promedio <= 4
# asistencia >= 85%
# reconocimiento == "Si"

# nota_promedio >= 4
# asistencia <= 85%
# reconocimiento == "Si"

# # 5
# promedio_estudiante = float(input("Ingrese su nota promedio: "))
# # 50
# asistencia_estudiante = float(input("Ingrese de 1 a 100 la asistencia del estudiante: "))/100
# # No
# reconocimiento_estudiante = input("¿Ha ganado el estudiante algún reconocimiento académico durante el año? (Si/No): ")

# if (promedio_estudiante >= 4.0 and asistencia_estudiante >= 0.85) or (reconocimiento_estudiante.lower() == "Si") and (promedio_estudiante >= 4.0 or asistencia_estudiante >= 0.85):
#     print("¡Felicidades! El Estudiante puede participar en el torneo académico.")
# else:
#     print("El Estudiante no cumple con los requisitos para participar en el torneo académico.")

# Un banco está evaluando solicitudes de crédito bajo ciertas condiciones. Se aprueba el crédito si la persona tiene ingresos mensuales superiores a USD 1.000 y no tiene reportes negativos en centrales de riesgo. Sin embargo, si la persona tiene un codeudor con buen historial crediticio, el crédito puede aprobarse aunque no cumpla una de las condiciones anteriores. El programa debe analizar la información ingresada y determinar si el crédito es aprobado o rechazado.

# Una tienda virtual ofrece descuentos a sus clientes bajo ciertas condiciones. El descuento se aplica si el cliente realiza una compra superior a USD 50 y además está registrado en la plataforma. También se otorga el descuento si el cliente tiene un cupón válido, sin importar el valor de la compra. El programa debe evaluar las condiciones y mostrar si el cliente recibe o no el descuento.

# valor_compra = >50 cliente_registrado = "Si"
# cupon_valido = "Si" 

# 100
valor_compra = float(input("Ingrese el valor de la compra en USD: "))
# Si
cliente_registrado = input("¿Está registrado en la plataforma? (Si/No): ")
# Si
cupon_valido = input("¿Tiene un cupón válido? (Si/No): ")

if (valor_compra > 50 and cliente_registrado.lower() == "si") or (cupon_valido.lower() == "si"):
    print("¡Felicidades! El cliente recibe el descuento.")
else:
    print("El cliente no cumple con las condiciones para recibir el descuento.")

