# aqui sera toda la logica para que el algoritmo funcione
import copy


class Linja:
    def __init__(self, tablero, jugador, cantidadMovimiento):
        self.tablero = tablero
        self.jugador = jugador
        self.cantidadMovimiento = cantidadMovimiento
        self.fichasMetaNegra = 0
        self.fichasMetaRoja = 0

    def impresion(self, listaDeListas: list):
        for fila in range(len(listaDeListas)):
            for columna in range(len(listaDeListas[0])):
                print(listaDeListas[fila][columna])
            print(
                f"Fichas meta negra: {self.fichasMetaNegra}".center(50, "-")
                + f"Fichas meta roja: {self.fichasMetaRoja}".center(50, "-"),
                end="\n",
            )

    def buscar_espacio_libre(self, nueva_columna):
        for fila in range(0, 6):
            if (
                self.tablero[fila][nueva_columna] == 0
            ):  # preguntamos si puede avanzar, si el espacio esta disponible, lo que hace el for es verificar desde el inicio de la columna si hay un espacio disponible
                return [fila, nueva_columna]
        return None

    def avanzarPosiblesMovimientos(self):
        actualidad = copy.deepcopy(self.tablero)
        # posicionFichaCol = 0
        # posicionFichaFila = 0
        arbolListasDeListas = []
        # listaFichasEncontradas = []

        # Recorrer la matriz por filas y columnas
        for fila in range(6):
            for columna in range(8):
                # Entra cuando la ficha es 1 o 2
                if actualidad[fila][columna] == self.jugador:
                    # Evaluar si el el jugador real
                    if self.jugador == 1:
                        nueva_columna = columna + self.cantidadMovimiento
                        if nueva_columna > 7:
                            nueva_columna = 7
                        nueva_posicion = self.buscar_espacio_libre(nueva_columna)
                        # Si no encontró una posición libre
                        if not nueva_posicion:
                            # Si la ficha roja ya sale del juego
                            if nueva_columna >= 7:
                                nuevo_tablero = copy.deepcopy(actualidad)
                                nuevo_tablero[fila][columna] = 0
                                arbolListasDeListas.append(nuevo_tablero)
                                self.fichasMetaRoja += 1
                        else:
                            nuevo_tablero = copy.deepcopy(actualidad)
                            nuevo_tablero[fila][columna] = 0
                            nuevo_tablero[nueva_posicion[0]][nueva_posicion[1]] = 1
                            arbolListasDeListas.append(nuevo_tablero)

                    # Evaluar si es la IA
                    else:
                        nueva_columna = columna - self.cantidadMovimiento
                        nueva_posicion = self.buscar_espacio_libre(nueva_columna)
                        # Si no encontró una posición libre
                        if not nueva_posicion:
                            # Si la ficha negra ya sale del juego
                            if nueva_columna <= 0:
                                nuevo_tablero = copy.deepcopy(actualidad)
                                nuevo_tablero[fila][columna] = 0
                                arbolListasDeListas.append(nuevo_tablero)
                                self.fichasMetaNegra += 1
                        else:
                            nuevo_tablero = copy.deepcopy(actualidad)
                            nuevo_tablero[fila][columna] = 0
                            nuevo_tablero[nueva_posicion[0]][nueva_posicion[1]] = 2
                            arbolListasDeListas.append(nuevo_tablero)
        self.impresion(arbolListasDeListas)

        # for fila in range(
        #     5, -1, -1
        # ):  # for para movernos en el tablero, filas, empieza desde 0 por indexaccion
        #     for columna in range(
        #         7, -1, -1
        #     ):  # for para movernos en el tablero, columnas
        #         if [
        #             fila,
        #             columna,
        #         ] not in listaFichasEncontradas:  # si ya se ha encontrado una ficha, ignorar esa posicion en especifico
        #             if (
        #                 2 == self.tablero[fila][columna]
        #             ):  # buscamos la ficha que mueve la ia, en este caso es el 2
        #                 posicionFichaFila = fila
        #                 posicionFichaCol = columna

        #                 listaFichasEncontradas.append(
        #                     [posicionFichaFila, posicionFichaCol]
        #                 )

        #                 if (
        #                     columna != 0
        #                 ):  # si esta en la ultima columna ignoramos pq ya llego a ultima casilla
        #                     if (
        #                         actualidad[fila][columna - self.cantidadMovimiento] == 0
        #                     ):  # preguntamos si puede avanzar, si el espacio esta disponible
        #                         nuevoTablero = copy.deepcopy(actualidad)
        #                         nuevoTablero[fila][
        #                             columna - self.cantidadMovimiento
        #                         ] = 2  # avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
        #                         nuevoTablero[posicionFichaFila][
        #                             posicionFichaCol
        #                         ] = 0  # como avanzamos tenemos que eliminar la ficha de donde estaba
        #                         arbolListasDeListas.append(nuevoTablero)
        #                         bandera = False
        #                         espacioLibre = True

        #                     else:
        #                         respuesta = self.buscar_espacio_libre(
        #                             columna - self.cantidadMovimiento
        #                         )

        #                         if (
        #                             respuesta
        #                         ):  # sise ha encontrado un espacio libre en la misma columna... si no se encuentra pss no puede saltar, pq lo minimo para saltar seria 2 si la siguiente columna de la anterior esta disponible
        #                             nuevoTablero = copy.deepcopy(actualidad)
        #                             nuevoTablero[respuesta[0]][
        #                                 respuesta[1]
        #                             ] = 2  # avanzmaos en el tablero, la ficha elegida en una posicion que si pueda estar
        #                             nuevoTablero[posicionFichaFila][
        #                                 posicionFichaCol
        #                             ] = 0  # como avanzamos tenemos que eliminar la ficha de donde estaba
        #                             arbolListasDeListas.append(nuevoTablero)
        #                             espacioLibre = True
        #                             # break

        #                         elif (
        #                             columna - self.cantidadMovimiento == 0
        #                         ):  # Si es la ulima columna ni no esta disponible
        #                             nuevoTablero = copy.deepcopy(actualidad)
        #                             nuevoTablero[posicionFichaFila][
        #                                 posicionFichaCol
        #                             ] = 0  # como avanzamos tenemos que eliminar la ficha de donde estaba
        #                             self.fichasMetaNegra += 1  # aumentamos las fichas que han llegando a la meta en 1 para tener un conteo
        #                             arbolListasDeListas.append(nuevoTablero)

        #                 if (
        #                     columna - self.cantidadMovimiento < 0
        #                 ):  # la ficha ya llego al final del tablero y se pierden los movimientos que se tengan hasta el momento
        #                     print("Out of bounds")
        #                     nuevoTablero = copy.deepcopy(actualidad)
        #                     nuevoTablero[posicionFichaFila][
        #                         posicionFichaCol
        #                     ] = 0  # como avanzamos tenemos que eliminar la ficha de donde estaba
        #                     arbolListasDeListas.append(nuevoTablero)
        #                     bandera = False
        #                     espacioLibre = True
        #                     self.fichasMetaNegra += 1

        # self.impresion(arbolListasDeListas)
        # print(listaFichasEncontradas)


matriz = [
    [1, 2, 2, 2, 2, 2, 2, 2],
    [1, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 2],
    [1, 1, 1, 1, 1, 1, 1, 2],
]
linja = Linja(tablero=matriz, jugador=1, cantidadMovimiento=2)
linja.avanzarPosiblesMovimientos()
