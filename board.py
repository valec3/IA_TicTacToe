import pygame
import copy
def empty_cells(cells):
    return [
        [r, c] for r in range(3) 
            for c in range(3) if cells[r][c] == 0
        ]
class Board:
    def __init__(self):
        # [[0,0,0],[0,0,0],[0,0,0]]
        self.cells = [[0,0,0],[0,0,0],[0,0,0]]
        self.empty_sqrs = self.cells 
        self.played = 0

    def final_state(self):
        for c in range(3):
            if self.cells[0][c] == self.cells[1][c] == self.cells[2][c] != 0:
                return self.cells[0][c]
        for r in range(3):
            if self.cells[r][0] == self.cells[r][1] == self.cells[r][2] != 0:
                return self.cells[r][0]
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != 0:
            return self.cells[0][0]
        if self.cells[2][0] == self.cells[1][1] == self.cells[0][2] != 0:
            return self.cells[2][0]
        return 0

    def add_go(self,player,row,col):
        """Agrega las fichas segun el jugador

        Args:
            player (int): numero de jugador
            row (int): nmr de fila
            col (int): nmr de columna
        """
        self.cells[row][col]=player
        self.played += 1

    def empty_cell(self,row,col):
        return self.cells[row][col] == 0

    def get_empty_cell(self):
        return empty_cells(self.cells)
    # REFACTORING
    
    def is_full_board(self):
        return self.played == 9 #true si esta lleno 
    
    def isempty(self):
        return self.played == 0