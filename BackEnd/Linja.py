

#aqui sera toda la logica para que el algoritmo funcione
import copy

arbolListasDeListas = []


class Linja:

    def __init__(self, tablero, cantidadMovimiento):

        self.tablero = tablero
        self.cantidadMovimiento = cantidadMovimiento
    
    def avanzarPosiblesMovimientos(self):

        actualidad = self.tablero

        espacioLibre = False

        posicionFichaCol = 0

        posicionFichaFila = 0

        for ficha in range(1, 13): #for para ver los movimientos de las 12 fichas se toma desde el 1 porque el cero en el tablero es un espacio vacio

            for fila in range (0, 6): #for para movernos en el tablero, filas, empieza desde 0 por indexaccion

                for columna in range(0, 8): #for para movernos en el tablero, columnas

                    if ficha == self.tablero[fila][columna]: #buscamos la ficha

                        posicionFichaFila = fila
                        posicionFichaCol = columna

                        if columna != 7: # si esta en la ultima columna ignoramos pq ya llego a ultima casilla
                            if self.cantidadMovimiento == 1: #si la cantidad de movimiento que se puede realizar es de 1, es decir, una casilla
                                if actualidad[fila][columna + 1] == 0: #preguntamos si puede avanzar, si el espacio esta disponible
                                    nuevoTablero = copy.deepcopy(actualidad)
                                    nuevoTablero[fila][columna + 1] = ficha #avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
                                    nuevoTablero[posicionFichaFila][posicionFichaCol] = 0 #como avanzamos tenemos que eliminar la ficha de donde estaba
                                    espacioLibre = True
                                    break
                                
                                else: 
                                    for aux in range(0, 6): #hacemos un for, ya que si el espacio directamente al frente no esta disponible debemos de encontrar un espacio en esa misma columna

                                        if actualidad[aux][columna + 1] == 0: #preguntamos si puede avanzar, si el espacio esta disponible, lo que hace el for es verificar desde el inicio de la columna si hay un espacio disponible
                                            nuevoTablero = copy.deepcopy(actualidad)
                                            nuevoTablero[aux][columna + 1] = ficha #avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
                                            nuevoTablero[posicionFichaFila][posicionFichaCol] = 0 #como avanzamos tenemos que eliminar la ficha de donde estaba
                                            espacioLibre = True
                                            break
                            
                            elif self.cantidadMovimiento > 0 and self.cantidadMovimiento != 1: #si la cantidad de movimientos es diferente a 1 y mayor a cero
                                
                                if actualidad[fila][columna + self.cantidadMovimiento] == 0: #preguntamos si puede avanzar, si el espacio esta disponible
                                    nuevoTablero = copy.deepcopy(actualidad)
                                    nuevoTablero[fila][columna + self.cantidadMovimiento] = ficha #avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
                                    nuevoTablero[posicionFichaFila][posicionFichaCol] = 0 #como avanzamos tenemos que eliminar la ficha de donde estaba
                                    espacioLibre = True
                                    break
                                
                                else: 
                                    for aux in range(0, 6): #hacemos un for, ya que si el espacio directamente al frente no esta disponible debemos de encontrar un espacio en esa misma columna

                                        if actualidad[aux][columna + self.cantidadMovimiento] == 0: #preguntamos si puede avanzar, si el espacio esta disponible, lo que hace el for es verificar desde el inicio de la columna si hay un espacio disponible
                                            nuevoTablero = copy.deepcopy(actualidad)
                                            nuevoTablero[aux][columna + self.cantidadMovimiento] = ficha #avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
                                            nuevoTablero[posicionFichaFila][posicionFichaCol] = 0 #como avanzamos tenemos que eliminar la ficha de donde estaba
                                            espacioLibre = True
                                            break

                            
                            if espacioLibre == True: #Si hay espacio libre en la siguiente columna y ya se realizo el cambio

                                pass # añadir logica para verificar que sea un movimiento valido

                            else: #si entra a este else es que no hay espacio libre  en la columna que tiene que avanzar segun la cantidad de movimientos que tenga
                                
                                pass # añadir logica para "saltar" esa columna y verificar en las siguientes para poder avanzar en el juego

                                        #tener encuenta que ya saltar se considera un movimiento


                        


                            

