from tkinter import Tk
from tkinter.filedialog import askopenfilename


def seleccionar_archivo():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter

    nombre_archivo = askopenfilename(
        title="Seleccionar archivo de texto",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
    )

    root.destroy()  # Cierra la ventana principal de tkinter

    if nombre_archivo:
        return leer_archivo(nombre_archivo)
    else:
        print("No se seleccionó ningún archivo.")
        return None


def leer_archivo(nombre_archivo):
    matriz = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            fila = [int(digito) for digito in linea.strip()]
            matriz.append(fila)
            print(fila)
    return matriz
