# Se desea reforestar un bosque cuya superficie se mide en hectáreas. Solicite al usuario la superficie del bosque en hectáreas y, según el tamaño, aplique la siguiente distribución de árboles:   
# Superficie mayor a 1.000.000 m²
# 70 % pino, 20 % oyamel, 10 % cedro
# Superficie menor o igual a 1.000.000 m²
# 50 % pino, 30 % oyamel, 20 % cedro
# Datos de densidad de siembra:
# En 10 m² caben 8 pinos.
# En 15 m² caben 15 oyameles.
# En 18 m² caben 10 cedros.
# Una hectárea equivale a 10.000 m².

# 30
tamano_superficie_terreno = float(input("Ingrese la superficie del bosque en hectáreas: "))

# Convertir hectáreas a metros cuadrados
# 30*10000 = 300.000
total_metros_cuadrados = tamano_superficie_terreno * 10000 

# 300.000
if total_metros_cuadrados <= 1000000:
    #  300.000*0.5 = 150.000   
    pino = total_metros_cuadrados * 0.5
    # 300.000*0.3 = 90.000
    oyamel = total_metros_cuadrados * 0.3
    # 300.000*0.2 = 60.000
    cedro = total_metros_cuadrados * 0.2
else:
    pino = total_metros_cuadrados * 0.7
    oyamel = total_metros_cuadrados * 0.2
    cedro = total_metros_cuadrados * 0.1

# (150.000/10)*8 = 120.000
total_pino = (pino / 10) * 8
# (90.000/15)*15 = 90.000
total_oyamel = (oyamel / 15) * 15
# (60.000/18)*10 = 33.333,33
total_cedro = (cedro / 18) * 10

print(f"Distribución de árboles para reforestar del Bosque:")
print(f"Superficie Total del Bosque: {total_metros_cuadrados:,.2f} m²")
print(f"Total de Superficie de Pino: {pino:,.2f} m²,  Total de Pinos es de ({total_pino:,.2f})")
print(f"Total de Superficie de Oyamel: {oyamel:,.2f} m², Total de Oyameles es de ({total_oyamel:,.2f})")
print(f"Total de Superficie de Cedro: {cedro:,.2f} m², Total de Cedros es de ({total_cedro:,.2f})")

