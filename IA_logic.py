import sys
import random
import numpy as np 
from minimax import minimax
class IA:
    """Clase para manejar la logica de la IA del juego
    """
    def __init__(self,player=2,level = 1):
        self.player=player
        self.level = level
    def move_rnd(self,cuad_vacio):
        if len(cuad_vacio) > 1:
            idx = random.randrange(0,len(cuad_vacio))
            return cuad_vacio[idx]
        
    def eval(self,board_empty,board):
        """Jugar segun el modo de dificultad

        Args:
            board (_type_): _description_
        """
        if self.level == 0:
            # Modo aleatorio 
            return self.move_rnd(board_empty)
        else:
            # minimax
            print( minimax(board,board_empty,False))