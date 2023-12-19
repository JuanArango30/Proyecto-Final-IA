

class nodo:

    def __init__(self, tablero, heuristica, movAdicional):

        self.tablero = tablero
        self.heuristica = heuristica
        self.movAdicional = movAdicional
    

    def __str__(self):
        

        return "tablero: {} \n Heuristica: {} \n movimiento Adicional: {} \n".format(self.tablero, self.heuristica, self.movAdicional)
    

    