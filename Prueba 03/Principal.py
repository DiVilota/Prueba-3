import Funciones as f
jugadores = []
tipo = ['principiante', 'anvanzado', 'experto'] 
juego = ['valorant', 'fortnite', 'fifa']
while True:
    print("[1]  Registrar puntajes torneo")
    print("[2]  Listar todos los puntajes")
    print("[3]  Imprimir por tipo")
    print("[4]  Salir del pograma ...")
    try:
        opc = int(input("Seleccione una opción: "))
        if opc < 0 or opc > 4:
            print("Opción NO válida!!")
    except ValueError:
            print("Opción DEBE ser un número!!")
            

    if opc == 1:
        f.registro_puntajes(jugadores,tipo, juego)

    if opc == 2:
        f.listar_puntajes(jugadores,tipo, juego)

    if opc == 3:
        f.imprimir_tipo(jugadores,tipo, juego)

    if opc == 4:
        print("Hasta pronto!")
        break
    



    