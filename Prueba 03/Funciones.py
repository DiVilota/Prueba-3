
def registro_puntajes(jugadores, tipo, juego):
 id_jugador = input("Escribe el ID del jugador: ")                    
 nombre = str(input("Escribe el nombre y el apellido del jugador: "))    

 juego_user = input("Ingrese el Juego en cual participa: valorant/fortnite/fifa: ").lower()
 flag = False
 for juego_user in juego:
    if juego_user == [juego]:
     print("Juego ingresado correctamente")
    flag = True
 else:
    print("No se pudo registrar el juego..")

 puntos = input("Ingrese el puntaje obtenido: ")

 tipo_user = input("Ingrese el nivel de los jugadores:principiante/avanzado/experto: ").lower()
 for tipo_user in tipo:
    if tipo_user == [tipo]:
       print("Nivel ingresado correctamente")
 else:
    print("Tipo NO válido!!") 

    jugador = {
       id_jugador : 'ID',
       nombre : 'nombre',
       juego_user : 'Juego',
       tipo_user : 'tipo',
       puntos : 'puntaje'
    }
 jugadores.append(jugador)
 print(jugadores)

def listar_puntajes(jugadores, tipo, juego):
   for jugador in {'puntos'}:
      print(jugador)

def imprimir_tipo():
    print()
