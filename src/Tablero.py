import copy
import pygame
import sys
import os

# Necesario para hacer visibles los archivos entre front y back
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Lector import seleccionar_archivo
from Linja import Linja
from Minimax import minimax, heuristica

# Tablero por archivo de texto (se abre seleccionar archivo antes de iniciar el juego)
board_from_file = seleccionar_archivo()

pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 680

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Linja")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)  # Color de las celdas del tablero
RED = (255, 0, 0)
BLACK = (0, 0, 0)
HALO_COLOR = (100, 235, 52)


FONT_SIZE = 30
font = pygame.font.Font(None, FONT_SIZE)  # Fuente para el texto


# Dimensiones del tablero
ROWS = 6
COLS = 8
CELL_SIZE = 100


board = 0

if board_from_file:
    board = copy.deepcopy(board_from_file)
else:
    board = [
        [1, 2, 2, 2, 2, 2, 2, 2],
        [1, 0, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 0, 2],
        [1, 1, 1, 1, 1, 1, 1, 2],
    ]  # Tablero inicial vacio

linja = Linja(tablero=board, jugador=1)
board = linja.tablero


# Dibuja el tablero creando una cuadricula
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(
                screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
            pygame.draw.rect(
                screen,
                BLACK,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                1,
            )


def draw_pieces(board, selected_piece):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:  # Suponiendo que 1 representa una ficha roja
                pygame.draw.circle(
                    screen,
                    RED,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2,
                    ),
                    CELL_SIZE // 3,
                )
            elif board[row][col] == 2:  # Suponiendo que 2 representa una ficha negra
                pygame.draw.circle(
                    screen,
                    BLACK,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2,
                    ),
                    CELL_SIZE // 3,
                )

            if selected_piece:
                pygame.draw.circle(
                    screen,
                    HALO_COLOR,
                    (
                        selected_piece[1] * CELL_SIZE + CELL_SIZE // 2,
                        selected_piece[0] * CELL_SIZE + CELL_SIZE // 2,
                    ),
                    CELL_SIZE // 3 + 2,
                    width=4,
                )


# Función para seleccionar una ficha
def select_piece(x, y):
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    if board[row][col] and board[row][col] == 1:
        return row, col
    return None


# Función que deselecciona una pieza por si el usuario desea cambiar
def deselect_piece():
    global selected_piece
    selected_piece = None


# Función para mover una ficha seleccionada
def move_piece(selected, x, y):
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    if (
        selected
        and not board[row][col]
        and linja.turnos_restantes > 0
        and selected[1] + linja.cantidadMovimiento == col
        and col != 7
    ):  # Por ahora, simplemente mover si la celda está vacía
        if col > selected[1]:
            board[row][col] = board[selected[0]][selected[1]]
            board[selected[0]][selected[1]] = 0
            cal_movements(board, (row, col))
            cal_turn()
    elif (
        selected
        and linja.turnos_restantes > 0
        and selected[1] + linja.cantidadMovimiento >= col
        and col == 7
    ):
        board[selected[0]][selected[1]] = 0
        linja.turnos_restantes = 0
        linja.fichasMetaRoja += 1
        cal_turn()


def cal_movements(board, new_pos_piece):
    contador = 0
    for row in range(ROWS):
        for col in range(COLS):
            if (new_pos_piece[1] == col) and (board[row][col]):
                contador += 1
    linja.turnos_restantes -= 1

    linja.cantidadMovimiento = contador - 1

    if linja.cantidadMovimiento == 0:
        linja.cantidadMovimiento = 1
        linja.turnos_restantes = 0


def cal_turn():
    if linja.jugador == 1 and linja.turnos_restantes == 0:
        linja.juego_terminado = linja.fin_del_juego()
        linja.jugador = 2
        linja.cantidadMovimiento = 1
        linja.turnos_restantes = 2
    print(f"jugador: {linja.jugador}")


selected_piece = None


def main():
    global select_piece
    selected_piece = None

    running = True
    while running:
        # if linja.jugador == 1 and not linja.juego_terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and linja.jugador == 1
                and not linja.juego_terminado
            ):
                x, y = pygame.mouse.get_pos()

                if pygame.mouse.get_pressed()[0]:  # Botón izquierdo del mouse
                    if not selected_piece:
                        selected_piece = select_piece(x, y)

                    else:
                        move_piece(selected_piece, x, y)
                        selected_piece = None

                elif pygame.mouse.get_pressed()[2]:  # Botón derecho del mouse
                    print(f"jugador: {linja.jugador}")
                    deselect_piece()
                    selected_piece = None

            elif linja.jugador == 2 and not linja.juego_terminado:
                global board
                print(f"Tablero viejo: \n{board}")
                new_board = minimax(linja, 2, float("-inf"), float("inf"))[0]
                print(f"Tablero nuevo: \n{new_board.tablero}")
                linja.actualizar_juego(new_board)
                board = linja.tablero
                linja.jugador = 1
                linja.turnos_restantes = 2
                linja.cantidadMovimiento = 1

        # elif linja.juego_terminado:
        #     # print("El juego ha terminado")
        #     clock.tick(0)

        screen.fill(BLACK)

        draw_board()
        draw_pieces(board, selected_piece)

        # Izquierda
        text_surface = font.render(
            f"Fichas negras afuera: {linja.fichasMetaNegra}", True, (255, 255, 255)
        )
        screen.blit(text_surface, (10, SCREEN_HEIGHT - FONT_SIZE))

        text_surface2 = font.render(
            f"Fichas rojas afuera: {linja.fichasMetaRoja}", True, (255, 255, 255)
        )
        screen.blit(text_surface2, (10, SCREEN_HEIGHT - 60))

        # Centro
        if linja.juego_terminado:
            text_surface = font.render(
                f"¡Ganan las {"rojas!" if heuristica(linja)[1] > heuristica(linja)[2] else "negras!"}", True, (255, 255, 255)
            )
            screen.blit(text_surface, (320, SCREEN_HEIGHT - 60))

            text_surface2 = font.render(
                f"Puntuación: {max(heuristica(linja))}", True, (255, 255, 255)
            )
            screen.blit(text_surface2, (340, SCREEN_HEIGHT - FONT_SIZE))

        # Derecha
        text_surface = font.render(
            f"Fichas por mover: {linja.turnos_restantes}", True, (255, 255, 255)
        )
        screen.blit(text_surface, (SCREEN_WIDTH - 210, SCREEN_HEIGHT - 60))

        text_surface2 = font.render(
            f"Casillas a mover: {linja.cantidadMovimiento}", True, (255, 255, 255)
        )
        screen.blit(text_surface2, (SCREEN_WIDTH - 210, SCREEN_HEIGHT - FONT_SIZE))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
