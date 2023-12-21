from Linja import Linja
import copy


def heuristica(tablero_linja: Linja) -> int:
    tablero = tablero_linja.tablero
    puntaje_rojas = tablero_linja.fichasMetaRoja * 5
    puntaje_negras = tablero_linja.fichasMetaNegra * 5

    # Calcular puntaje de las negras
    for columna in range(4):
        for fila in range(6):
            if tablero[fila][columna] == 2:
                if columna == 0:
                    puntaje_negras -= 5
                if columna == 1:
                    puntaje_negras -= 3
                if columna == 2:
                    puntaje_negras -= 2
                if columna == 3:
                    puntaje_negras -= 1

    # Calcular puntaje de las rojas
    for columna in range(7, 3, -1):
        for fila in range(6):
            if tablero[fila][columna] == 1:
                if columna == 7:
                    puntaje_rojas += 5
                if columna == 6:
                    puntaje_rojas += 3
                if columna == 5:
                    puntaje_rojas += 2
                if columna == 4:
                    puntaje_rojas += 1
    print(f"Heuristica: {puntaje_rojas + puntaje_negras}")
    return puntaje_rojas + puntaje_negras


def minimax(tablero_linja: Linja, jugador, profundidad):
    if profundidad == 2 or tablero_linja.fin_del_juego():
        print("Entró")
        return tablero_linja.tablero, int(heuristica(tablero_linja))

    mejor_jugada = None

    if jugador == 1:
        maximo = float("-inf")
        jugadas = tablero_linja.posibles_movimientos()
        for jugada in jugadas:
            print(profundidad)
            tablero_linja_aux, valor_heuristica = minimax(jugada, 2, profundidad + 1)
            print(valor_heuristica)
            if valor_heuristica >= maximo:
                maximo = valor_heuristica
                mejor_jugada = jugada.tablero
        return mejor_jugada, valor_heuristica
    else:
        minimo = float("inf")
        jugadas = tablero_linja.posibles_movimientos()
        for jugada in jugadas:
            print(profundidad)
            tablero_linja_aux, valor_heuristica = minimax(jugada, 2, profundidad + 1)
            if valor_heuristica < minimo:
                minimo = valor_heuristica
                mejor_jugada = jugada.tablero
        return mejor_jugada, valor_heuristica


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

# res = minimax(linja, 2, 0)
# print(res[0])
# print(res[1])
