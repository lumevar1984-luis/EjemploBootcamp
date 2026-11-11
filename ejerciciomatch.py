# Opcion 1
# print("1.Suma\n2.Resta\n3.Multiplicación\n4.División")
# # 3
# opcion=int(input("Ingrese la opción: "))
# # 100
# numero1=int(input("Digite un número: "))
# # 2
# numero2=int(input("Digite otro número: "))

# if opcion == 1:
#     resultado= numero1 + numero2
#     print(f"El resultado es: {resultado:.1f}")
# elif opcion == 2:
#     resultado=numero1 - numero2
#     print(f"El resultado es: {resultado:.1f}")
# elif opcion == 3:
# #               100 * 2     
#     resultado= numero1 * numero2
#     print(f"El resultado es: {resultado:.1f}")
# elif opcion == 4:
#     resultado= numero1 / numero2
#     print(f"El resultado es: {resultado:.1f}")
# elif opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
#     print("Opción no válida ❌")

# Opcion 2

# print("\nOpciones\n1.Suma\n2.Resta\n3.Multiplicación\n4.División")

# opcion = int(input("Ingrese la opción: "))

# if opcion < 1 or opcion > 4:
#     print("Opción no válida ❌")
# else:
#     numero1 = int(input("Digite el primer número: "))
#     numero2 = int(input("Digite el segundo número: "))
#     if opcion == 1:
#         resultado = numero1 + numero2
        
#     elif opcion == 2:
#         resultado = numero1 - numero2
        
#     elif opcion == 3:
#         resultado = numero1 * numero2
        
#     elif opcion == 4:
#         if numero2 != 0:
#             resultado = numero1 / numero2
#         else: 
#             resultado = "No se puede realizar la operación."
#     if type(resultado) == str:
#         print(resultado)
#     else:    
#         print(f"El resultado es: {resultado}\n")

# Opcion 3

# print("\nOpciones\n1.Suma\n2.Resta\n3.Multiplicación\n4.División")

# opcion = int(input("Ingrese la opción: "))

# numero1 = int(input("Digite el primer número: "))
# numero2 = int(input("Digite el segundo número: "))

# resultado = False

# match opcion:

#     case 1:
#         resultado = numero1 + numero2
        
#     case 2:
#         resultado = numero1 - numero2
        
#     case 3:
#         resultado = numero1 * numero2
        
#     case 4:
#         resultado = numero1 / numero2 
#     case _:
#         pass
    
# if resultado == False:
#     print("Opción no Válida ❌")

# else:
#     print(f"**El Resultado de la Operación es: {resultado:,.1f}**")

# Opcion 4

print("\nOpciones\n1.Suma\n2.Resta\n3.Multiplicación\n4.División")

opcion = int(input("Ingrese la opción: (1-4) "))

if opcion <= 0 or opcion >= 4:
    print("Opción no válida ❌")
else:

    numero1 = int(input("Digite el primer número: "))
    numero2 = int(input("Digite el segundo número: "))


    match opcion:

        case 1:
            resultado = numero1 + numero2
            print(f"**El Resultado de la Operación es: {resultado:,.1f}**")
        case 2:
            resultado = numero1 - numero2
            print(f"**El Resultado de la Operación es: {resultado:,.1f}**")
        case 3:
            resultado = numero1 * numero2
            print(f"**El Resultado de la Operación es: {resultado:,.1f}**")
        case 4:
            if numero2 == 0:
                resultado_mod= 0
                print(" ❌ Error: No se puede dividir entre cero")

            else:
                resultado = numero1 / numero2
                print(f"**El Resultado de la Operación es: {resultado:,.1f}**")








