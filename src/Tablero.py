import copy
import pygame
import sys
import os

# Necesario para hacer visibles los archivos entre front y back
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Lector import seleccionar_archivo
from Linja import Linja
from Minimax import minimax

# Tablero por archivo de texto (se abre seleccionar archivo antes de iniciar el juego)
board_from_file = seleccionar_archivo()

pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 630

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
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]  # Tablero inicial vacio

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
    ):  # Por ahora, simplemente mover si la celda está vacía
        if col > selected[1]:
            board[row][col] = board[selected[0]][selected[1]]
            board[selected[0]][selected[1]] = None
            cal_movements(board, (row, col))
    elif (
        selected
        and linja.turnos_restantes > 0
        and selected[1] + linja.cantidadMovimiento >= col
        and col == 7
    ):
        board[selected[0]][selected[1]] = None
        linja.turnos_restantes = 0


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


def AITurn():
    linja.jugador = 2
    linja.cantidadMovimiento = 1
    linja.turnos_restantes = 2
    linja.posibles_movimientos()


selected_piece = None


def main():
    global select_piece
    selected_piece = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:  # Botón izquierdo del mouse
                    if not selected_piece:
                        selected_piece = select_piece(x, y)
                    else:
                        move_piece(selected_piece, x, y)
                        selected_piece = None
                elif pygame.mouse.get_pressed()[2]:  # Botón derecho del mouse
                    deselect_piece()
                    selected_piece = None

        screen.fill(BLACK)

        draw_board()
        draw_pieces(board, selected_piece)

        text_surface = font.render(
            f"Fichas por mover: {linja.turnos_restantes}", True, (255, 255, 255)
        )
        screen.blit(
            text_surface, (10, SCREEN_HEIGHT - FONT_SIZE + 5)
        )  # 10 píxeles desde el borde y 10 píxeles por encima del borde inferior

        text_surface2 = font.render(
            f"Casillas a mover: {linja.cantidadMovimiento}", True, (255, 255, 255)
        )
        screen.blit(
            text_surface2, (SCREEN_WIDTH - 300, SCREEN_HEIGHT - FONT_SIZE + 5)
        )  # 150 píxeles desde el borde derecho y 10 píxeles por encima del borde inferior

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
