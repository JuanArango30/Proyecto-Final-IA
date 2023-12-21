# aqui sera toda la logica para que el algoritmo funcione
import copy


class Linja:
    def __init__(
        self,
        tablero,
        jugador=2,
        turnos_restantes=2,
        cantidadMovimiento=1,
        fichasMetaRoja=0,
        fichasMetaNegra=0,
    ):
        self.tablero = tablero
        self.jugador = jugador
        self.turnos_restantes = turnos_restantes
        self.cantidadMovimiento = cantidadMovimiento
        self.fichasMetaNegra = fichasMetaNegra
        self.fichasMetaRoja = fichasMetaRoja

    def get_tablero(self):
        return copy.deepcopy(self.tablero)

    def fin_del_juego(self) -> bool:
        # Búsqueda de la ficha roja de más a la izquierda (porque terminan a la derecha)
        menor_columna_rojas = 7
        for columna in range(7, -1, -1):
            for fila in range(5, -1, -1):
                if self.tablero[fila][columna] == 1:
                    menor_columna_rojas = columna
                    break
        # Búsqueda de la ficha negra de más a la derecha (porque terminan a la izquierda)
        mayor_columna_negras = 0
        for columna in range(8):
            for fila in range(6):
                if self.tablero[fila][columna] == 2:
                    mayor_columna_negras = columna
                    break
        return menor_columna_rojas > mayor_columna_negras

    def buscar_espacio_libre(self, nueva_columna):
        for fila in range(0, 6):
            if (
                self.tablero[fila][nueva_columna] == 0
            ):  # preguntamos si puede avanzar, si el espacio esta disponible, lo que hace el for es verificar desde el inicio de la columna si hay un espacio disponible
                return [fila, nueva_columna]
        return None

    def cantidad_proximo_movimiento(self, nueva_columna):
        cantidad_fichas = 0
        for fila in range(0, 6):
            # Contamos las fichas de la columna
            if self.tablero[fila][nueva_columna] != 0:
                cantidad_fichas += 1

        # Si la ficha cae en una columna vacía, se cambia el jugador y se restablece la cantidad de turnos
        if cantidad_fichas == 1 or self.cantidadMovimiento == 0:
            self.cantidadMovimiento = 1
            self.turnos_restantes = 2
            self.jugador = 1 if self.jugador == 2 else 2
        else:
            # Si la columna tiene más fichas y hay otro turno, se fija la cantidad del
            # proximo movimiento
            if self.turnos_restantes == 2:
                self.turnos_restantes = 1
                self.cantidadMovimiento = cantidad_fichas - 1

            # Si solo le quedaba un turno, se pasa el turno al siguiente jugador
            else:
                self.cantidadMovimiento = 1
                self.turnos_restantes = 2
                self.jugador = 1 if self.jugador == 2 else 2

    def calcular_movimiento(self, fila_ficha, columna_ficha):
        # Entra cuando la ficha es 1 o 2
        if self.tablero[fila_ficha][columna_ficha] == self.jugador:
            # Evaluar si el el jugador real
            if self.jugador == 1:
                nueva_columna = columna_ficha + self.cantidadMovimiento
                if nueva_columna > 7:
                    nueva_columna = 7
                nueva_posicion = self.buscar_espacio_libre(nueva_columna)
                # Si no encontró una posición libre
                if not nueva_posicion:
                    # Si la ficha roja ya sale del juego
                    if nueva_columna >= 7:
                        # Se actualiza una copia del tablero con el movimiento
                        nuevo_tablero = copy.deepcopy(self.tablero)
                        nuevo_tablero[fila_ficha][columna_ficha] = 0

                        # Se crea una nueva instancia con el tablero actualizado
                        linja_siguiente_movimiento = Linja(
                            nuevo_tablero,
                            self.jugador,
                            self.turnos_restantes,
                            self.cantidadMovimiento,
                            self.fichasMetaRoja,
                            self.fichasMetaNegra,
                        )

                        linja_siguiente_movimiento.cantidadMovimiento = 0

                        # Se calcula si hay próximo movimiento y quién sigue
                        linja_siguiente_movimiento.cantidad_proximo_movimiento(
                            nueva_columna
                        )
                        linja_siguiente_movimiento.fichasMetaRoja += 1

                        # Se retorna la instancia actualizada
                        return linja_siguiente_movimiento

                # Si se encuentran espacios disponibles
                else:
                    # Se actualiza una copia del tablero con el movimiento
                    nuevo_tablero = copy.deepcopy(self.tablero)
                    nuevo_tablero[fila_ficha][columna_ficha] = 0
                    nuevo_tablero[nueva_posicion[0]][nueva_posicion[1]] = 1

                    # Se crea una nueva instancia con el tablero actualizado
                    linja_siguiente_movimiento = Linja(
                        nuevo_tablero,
                        self.jugador,
                        self.turnos_restantes,
                        self.cantidadMovimiento,
                        self.fichasMetaRoja,
                        self.fichasMetaNegra,
                    )

                    # Se calcula si hay próximo movimiento y quién sigue
                    linja_siguiente_movimiento.cantidad_proximo_movimiento(
                        nueva_columna
                    )

                    # Se retorna la instancia actualizada
                    return linja_siguiente_movimiento

            # Evaluar si es la IA
            else:
                nueva_columna = columna_ficha - self.cantidadMovimiento
                if nueva_columna < 0:
                    nueva_columna = 0
                nueva_posicion = self.buscar_espacio_libre(nueva_columna)
                # Si no encontró una posición libre
                if not nueva_posicion:
                    # Si la ficha roja ya sale del juego
                    if nueva_columna <= 0:
                        # Se actualiza una copia del tablero con el movimiento
                        nuevo_tablero = copy.deepcopy(self.tablero)
                        nuevo_tablero[fila_ficha][columna_ficha] = 0

                        # Se crea una nueva instancia con el tablero actualizado
                        linja_siguiente_movimiento = Linja(
                            nuevo_tablero,
                            self.jugador,
                            self.turnos_restantes,
                            self.cantidadMovimiento,
                            self.fichasMetaRoja,
                            self.fichasMetaNegra,
                        )

                        linja_siguiente_movimiento.cantidadMovimiento = 0

                        # Se calcula si hay próximo movimiento y quién sigue
                        linja_siguiente_movimiento.cantidad_proximo_movimiento(
                            nueva_columna
                        )
                        linja_siguiente_movimiento.fichasMetaNegra += 1

                        # Se retorna la instancia actualizada
                        return linja_siguiente_movimiento

                # Si se encuentran espacios disponibles
                else:
                    # Se actualiza una copia del tablero con el movimiento
                    nuevo_tablero = copy.deepcopy(self.tablero)
                    nuevo_tablero[fila_ficha][columna_ficha] = 0
                    nuevo_tablero[nueva_posicion[0]][nueva_posicion[1]] = 2

                    # Se crea una nueva instancia con el tablero actualizado
                    linja_siguiente_movimiento = Linja(
                        nuevo_tablero,
                        self.jugador,
                        self.turnos_restantes,
                        self.cantidadMovimiento,
                        self.fichasMetaRoja,
                        self.fichasMetaNegra,
                    )

                    # Se calcula si hay próximo movimiento y quién sigue
                    linja_siguiente_movimiento.cantidad_proximo_movimiento(
                        nueva_columna
                    )

                    # Se retorna la instancia actualizada
                    return linja_siguiente_movimiento
        return None

    def posibles_movimientos(self):
        primer_movimiento = []
        segundo_movimiento = []

        if not self.fin_del_juego():
            # Recorrer la matriz por filas y columnas (primer movimiento)
            for fila in range(6):
                for columna in range(8):
                    # Calcular el movimiento de la ficha actual
                    nuevo_tablero = self.calcular_movimiento(fila, columna)
                    if nuevo_tablero:
                        primer_movimiento.append(nuevo_tablero)
            # print("Primer movimiento".center(50, "-"))
            # self.impresion(primer_movimiento)
            # print("\n")

            # print("Segundo movimiento".center(50, "-"))

            # Recorrer las posibilidades del primer movimiento para el segundo movimiento
            i = 0  # Para propositos de print
            for tablero in primer_movimiento:
                # Recorrer la matriz por filas y columnas (primer movimiento)
                for fila in range(6):
                    for columna in range(8):
                        # Calcular el movimiento de la ficha actual
                        nuevo_tablero = tablero.calcular_movimiento(fila, columna)
                        if nuevo_tablero:
                            segundo_movimiento.append(nuevo_tablero)
                #             print(f"Posibilidades para el movimiento {i}")
                #             self.impresionSegundo(nuevo_tablero)
                # print("\n")
                i += 1

        # else:
        #     print("\n" + "Fin del juego".center(50, "-"), end="\n")

        return copy.deepcopy(segundo_movimiento)

    def impresion(self, lista_movimientos: list):
        for movimiento in lista_movimientos:
            for fila in range(6):
                print(movimiento.tablero[fila])
            print(
                f"Fichas meta negra: {movimiento.fichasMetaNegra}".center(50, "-")
                + f"Fichas meta roja: {movimiento.fichasMetaRoja}".center(50, "-"),
                end="\n",
            )

    def impresionSegundo(self, movimiento: list):
        for fila in range(6):
            print(movimiento.tablero[fila])
        print(
            f"Fichas meta negra: {movimiento.fichasMetaNegra}".center(50, "-")
            + f"Fichas meta roja: {movimiento.fichasMetaRoja}".center(50, "-"),
            end="\n",
        )


# matriz = [
#     [2, 2, 0, 0, 0, 0, 1, 1],
#     [2, 2, 0, 0, 0, 0, 1, 1],
#     [2, 2, 0, 0, 0, 0, 1, 1],
#     [2, 0, 0, 0, 1, 2, 0, 1],
#     [2, 2, 0, 0, 0, 0, 1, 1],
#     [2, 2, 0, 0, 0, 0, 1, 1],
# ]

# matriz = [
#     [1, 2, 2, 2, 2, 2, 2, 2],
#     [1, 0, 0, 0, 0, 0, 0, 2],
#     [1, 0, 0, 0, 0, 0, 0, 2],
#     [1, 0, 0, 0, 0, 0, 0, 2],
#     [1, 0, 0, 0, 0, 0, 0, 2],
#     [1, 1, 1, 1, 1, 1, 1, 2],
# ]
# linja = Linja(
#     matriz,
# )
# # linja.posibles_movimientos()
