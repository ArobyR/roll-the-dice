from random import randint
# 11 de marzo del 2020
# This is game 2...

""" AUTHOR == Gr0b1t:
                    Aroby
"""
game = "BIENVENIDO AL JUEGO"
print(game.center(100, "_"))

while True:

    lanzar = input("\nPULSE: " "S " "SI QUIERE JUGAR," " N " "SINO QUIERE JUGAR: " )
    
    aux = lanzar.lower()

    if aux == "n":
        print("Adios...")
        break

    # sino, si aux es diferente de "s" imprimir valor incorrecto y salir
    elif aux != "s":
        print("Valor incorrecto.")
        break

    # simulacion de lanzamiento
    if aux == "s":
        print("Lanzando el dado...")

    dado1 = randint(1, 6) 
    dado2 = randint(1, 6)
        
    # sumatoria de los dados
    sumatoria_3 = dado1 + dado2
    print("La sumatoria de los dados es:", sumatoria_3)

    # si la sumatoria de los dados es igual a 7 o igual a 12, entonces gana y finaliza el juego
    if sumatoria_3 == 7 or sumatoria_3 == 12:
        ganador = " HAS GANADO "
        print(ganador.center(100, "="))
        break

    # si es un numero impar diferente de 7 pierde y termina el juego
    if sumatoria_3 != 7 and sumatoria_3 % 2 != 0:
        perder = " HAS PERDIDO "
        print(perder.center(100, "*"))
        break

    # si es un numero par diferente de 12 
    if sumatoria_3 % 2 == 0 and sumatoria_3 != 12:
        print("\nTienes 5 intentos para conseguir el ultimo numero.")
        
        # 5 intentos
        intentos = 5
        
        while intentos > 0:
            
            # Imprimir intentos
            print(f"Intento {intentos}") 
            
            # simulacion de lanzamiento 2.0
            lanzamiento = input("PULSE S PARA LANZAR EL DADO: ")
            aux2 = lanzamiento.lower()
            
            if aux2 != "s":
                print("Valor incorrecto, adios.")
                break

            # Generacion de lanzamiento / numeros random
            dado3 = randint(1, 6)
            dado4 = randint(1, 6)
            sumatoria_4 = dado3 + dado4
            
            # Menos un intento
            intentos -= 1

            # si consigues el numero anterior ganas
            if sumatoria_4 == sumatoria_3:
                print("Has obtenido el mismo numero, por ende has ganado.")
                break
            
            # Si los dados son iguales/dobles mas un intento
            if dado3 == dado4:
                print("Ha conseguido un doble, eso quiere decir +1 intento.")
                intentos += 1 

            # si la suma de los dados es igual a 7 o 12, entonces pierde y el juego termina
            if sumatoria_4 == 7 or sumatoria_4 == 12:
                print("Ha perdido, ha conseguido un maravilloso:", sumatoria_4, " Hasta la proxima...")
                break
            
            # Imprimir la sumatoria de los dados en cada lanzamiento
            print("La sumatoria de los dados es igual: ", sumatoria_4)
            