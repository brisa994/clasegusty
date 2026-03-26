sonido = 343
velocidad = 1

while velocidad != 0:
    velocidad = float(input("Velocidad del avion (0 para salir): "))
    if velocidad == 0:
        print("Programa terminado.")
    elif velocidad > sonido:
        print("Resultado: Supersonico")
    else:
        print("Resultado: No supersonico")
