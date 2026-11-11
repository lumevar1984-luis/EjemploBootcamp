# Una tienda vende un producto que cuesta USD 10. Primero el programa debe preguntar si el producto está disponible (si o no). Si no está disponible, debe mostrar Producto agotado y no pedir nada más. Si está disponible, debe pedir el saldo de la persona (número entero): si el saldo es USD 10 o más, debe mostrar Compra exitosa; si es menor, debe mostrar Saldo insuficiente

producto_disponible = input("¿El producto está disponible? (si/no): ").lower()

if producto_disponible != "si" and producto_disponible != "no":
    print("Opción no válida ❌")
elif producto_disponible == "no":
    print("Producto agotado ❌")

if producto_disponible == "si":
    saldo_persona = int(input("Ingrese su saldo en USD: "))

    if saldo_persona >= 10:
        print("Compra exitosa ✅")
    else:
        print("Saldo insuficiente ❌")



