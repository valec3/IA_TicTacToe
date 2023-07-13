import sys
import random
import numpy as np 
import copy
from math import inf as infinity
from board import Board
from minimax import minimax
class IA:
    """Clase para manejar la logica de la IA del juego
    """
    def __init__(self,player=1,level = 1):
        self.player=player
        self.level = level
    def move_rnd(self,cuad):
        cuad_vacio = cuad.get_empty_cell()
        if len(cuad_vacio) > 1:
            idx = random.randrange(0,len(cuad_vacio))
            return cuad_vacio[idx]
        
    def eval(self,board):
        """Jugar segun el modo de dificultad

        Args:
            board (_type_): _description_
        """
        if self.level == 0:
            # Modo aleatorio 
            return self.move_rnd(board)
        else:
            # minimax
            profundidad = len(board.get_empty_cell())
            move = minimax(board.cells, profundidad, 1)

        return [move[0],move[1]] # row, col