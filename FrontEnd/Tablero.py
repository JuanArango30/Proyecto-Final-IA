# Necesario para hacer visibles los archivos entre front y back
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pygame
from BackEnd.Lector import seleccionar_archivo

# Tablero por archivo de texto (se abre seleccionar archivo antes de iniciar el juego)
board_from_file = seleccionar_archivo()

pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Linja")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)  # Color de las celdas del tablero
RED = (255, 0, 0)
BLACK = (0, 0, 0)
HALO_COLOR = (100, 235, 52)

# Dimensiones del tablero
ROWS = 6
COLS = 8
CELL_SIZE = 100


players_turn = True  # Variable que indica si es el turno del jugador
movements = 2  # Numero de movimientos disponibles (cantidad de fichas que puede mover en su turno)
num_cols_mover = 1  # Numero de columnas que se puede mover una ficha

board = (
    [[0 for _ in range(COLS)] for _ in range(ROWS)]
    if not board_from_file
    else board_from_file.copy()
)  # Tablero inicial vacio
board[0][0] = 1
board[0][1] = 2


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
    if board[row][col]:
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
        selected and not board[row][col]
    ):  # Por ahora, simplemente mover si la celda está vacía
        board[row][col] = board[selected[0]][selected[1]]
        board[selected[0]][selected[1]] = None


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

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
