

class nodo:

    def __init__(self, tablero, heuristica, movAdicional, hijos):

        self.tablero = tablero
        self.heuristica = heuristica
        self.movAdicional = movAdicional
        self.hijos =hijos
    

    def __str__(self):
        

        return "tablero: {} \n Heuristica: {} \n movimiento Adicional: {} \n".format(self.tablero, self.heuristica, self.movAdicional)
    




