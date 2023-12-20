

#aqui sera toda la logica para que el algoritmo funcione
import copy

arbolListasDeListas = []
listaFichasEncontradas =[]

class Linja:

    def __init__(self, tablero, cantidadMovimiento):

        self.tablero = tablero
        self.cantidadMovimiento = cantidadMovimiento
    
    def buscar_espacio_libre(self, columna):
        for fila in range(0, 6): 
            if self.tablero[fila][columna] == 0: #preguntamos si puede avanzar, si el espacio esta disponible, lo que hace el for es verificar desde el inicio de la columna si hay un espacio disponible
                return [fila, columna]
        return None

    def avanzarPosiblesMovimientosIA(self):

        actualidad = self.tablero

        espacioLibre = False

        posicionFichaCol = 0

        posicionFichaFila = 0

        for ficha in range(1, 13): #for para ver los movimientos de las 12 fichas se toma desde el 1 porque el cero en el tablero es un espacio vacio

            for fila in range (0, 6): #for para movernos en el tablero, filas, empieza desde 0 por indexaccion

                for columna in range(0, 8): #for para movernos en el tablero, columnas

                    if [fila, columna] not in listaFichasEncontradas: #si ya se ha encontrado una ficha, ignorar esa posicion en especifico

                        if 2 == self.tablero[fila][columna]: #buscamos la ficha que mueve la ia, en este caso es el 2

                            posicionFichaFila = fila
                            posicionFichaCol = columna

                            listaFichasEncontradas.append([posicionFichaFila, posicionFichaCol])

                            if columna != 7: # si esta en la ultima columna ignoramos pq ya llego a ultima casilla
                                if self.cantidadMovimiento == 1: #si la cantidad de movimiento que se puede realizar es de 1, es decir, una casilla
                                    if actualidad[fila][columna + 1] == 0: #preguntamos si puede avanzar, si el espacio esta disponible
                                        nuevoTablero = copy.deepcopy(actualidad)
                                        nuevoTablero[fila][columna + 1] = ficha #avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
                                        nuevoTablero[posicionFichaFila][posicionFichaCol] = 0 #como avanzamos tenemos que eliminar la ficha de donde estaba
                                        espacioLibre = True
                                        break
                                    
                                    else: 
                                        
                                        respuesta = self.buscar_espacio_libre(columna + 1)
                                        
                                        if respuesta: # sise ha encontrado un espacio libre en la misma columna... si no se encuentra pss no puede saltar, pq lo minimo para saltar seria 2 si la siguiente columna de la anterior esta disponible 
                                                nuevoTablero = copy.deepcopy(actualidad)
                                                nuevoTablero[respuesta[0]][respuesta[1]] = ficha #avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
                                                nuevoTablero[posicionFichaFila][posicionFichaCol] = 0 #como avanzamos tenemos que eliminar la ficha de donde estaba
                                                espacioLibre = True
                                                break
                                        
                                        

                                
                                elif self.cantidadMovimiento > 0 and self.cantidadMovimiento != 1: #si la cantidad de movimientos es diferente a 1 y mayor a cero
                                    
                                    bandera = True

                                    while bandera:
                                        try:
                                        
                                            if actualidad[fila][columna + self.cantidadMovimiento] == 0: #preguntamos si puede avanzar, si el espacio esta disponible
                                                nuevoTablero = copy.deepcopy(actualidad)
                                                nuevoTablero[fila][columna + self.cantidadMovimiento] = ficha #avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
                                                nuevoTablero[posicionFichaFila][posicionFichaCol] = 0 #como avanzamos tenemos que eliminar la ficha de donde estaba
                                                bandera = False
                                                espacioLibre = True
                                                break
                                            
                                            else:

                                                respuesta = self.buscar_espacio_libre(columna + 1)
                                        
                                                if respuesta: # sise ha encontrado un espacio libre en la misma columna... si no se encuentra pss no puede saltar, pq lo minimo para saltar seria 2 si la siguiente columna de la anterior esta disponible 
                                                    nuevoTablero = copy.deepcopy(actualidad)
                                                    nuevoTablero[respuesta[0]][respuesta[1]] = ficha #avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
                                                    nuevoTablero[posicionFichaFila][posicionFichaCol] = 0 #como avanzamos tenemos que eliminar la ficha de donde estaba
                                                    espacioLibre = True
                                                    break
                                                
                                        except:

                                            self.cantidadMovimiento -=1

                                
            if espacioLibre == True: #Si hay espacio libre en la siguiente columna y ya se realizo el cambio

                arbolListasDeListas.append(nuevoTablero)




                        


                            

