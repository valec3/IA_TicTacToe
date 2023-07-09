# Importar librerias
import pygame
import sys
import numpy as np
from config import Configuraciones
class Game:
    def __init__(self) -> None:
        """Inicializa el juego y crea los recursos del juego."""
        pygame.init()
        pygame.display.set_caption("Tic Tac Toe")
        
        self.game_active=False
        self.clock = pygame.time.Clock() #Controlar FPS
        self.config = Configuraciones() 
        self.ventana = pygame.display.set_mode(
            (self.config.ventana_width,self.config.ventana_height)
        )
        
        self.player_current= 1
        self.cells=np.zeros((3,3))
        self.cells_emp=self.cells
        self.comb_wins= [
                        [0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [2, 4, 6]
                        ]
        
    def show_board(self):
        """Dibuja el tablero 3x3
        """
        # Dibujar fondo del tablero
        pygame.draw.rect(self.ventana,
                        (255, 82, 82),
                        (self.config.board_lx,self.config.board_ty,self.config.board_sz_w,self.config.board_sz_w))
        
        # Dibujar lineas
        for i in range(4):
            pygame.draw.line(self.ventana,
                            self.config.board_color,
                            (self.config.board_lx+i*self.config.sqr_size,self.config.board_ty),
                            (self.config.board_lx+i*self.config.sqr_size,self.config.board_by)
                            ,7)
        for j in range(4):
            pygame.draw.line(self.ventana,
                            self.config.board_color,
                            (self.config.board_lx,self.config.board_ty+j*self.config.sqr_size),
                            (self.config.board_dx,self.config.board_ty+j*self.config.sqr_size)
                            ,7)
        
    def add_go(self,player,row,col):
        self.cells[row][col]=player
        self.change_turn()
        
    def draw_goes(self):
        """Dibuja las fichas de los jugadores
        """
        for r in range(3):
            for c in range(3):
                if self.cells[r][c] == 1:
                    # line 1
                    start_line = (self.config.cross_lls + c*self.config.sqr_size,
                                self.config.cross_lle + r*self.config.sqr_size)
                    end_line = (self.config.cross_lls + self.config.sqr_size-70+c*self.config.sqr_size,
                                self.config.cross_lle+self.config.sqr_size-70+r*self.config.sqr_size)
                    pygame.draw.line(self.ventana,self.config.cross_color,start_line,end_line,self.config.cross_w)
                    
                    # line 2
                    start_line2 = (self.config.cross_lls + c*self.config.sqr_size,
                                self.config.cross_lle+self.config.sqr_size-70+r*self.config.sqr_size) 
                    end_line2 = (self.config.cross_lls + self.config.sqr_size-70+c*self.config.sqr_size,
                                self.config.cross_lle + r*self.config.sqr_size)
                    pygame.draw.line(self.ventana,self.config.cross_color,start_line2,end_line2,self.config.cross_w)
                elif self.cells[r][c] == 2:
                    center = (self.config.circ_cr+c*self.config.sqr_size,self.config.circ_cc+r*self.config.sqr_size) 
                    pygame.draw.circle(
                        self.ventana, 
                        self.config.circ_color,
                        center,
                        self.config.circ_r,
                        self.config.circ_w
                    )
    def empty_cell(self,row,col):
        return self.cells[row][col] == 0
    def change_turn(self):
        self.player_current = self.player_current % 2 + 1
    def actualizar_ventana(self):
        """Actualizar imagenes en la ventana y mostrar ventana actual."""
        # Redibuja el fondo durante cada pasada por el bucle.
        self.ventana.fill(self.config.bg_color)
        self.ventana.blit(self.config.bg_imagen,(0,0))
        
        self.show_board()
        self.draw_goes()
        #Actualizar pantalla
        pygame.display.flip()
        
    def revisar_eventos(self):
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos=evento.pos
                    row=int((pos[1] - self.config.board_ty)// self.config.sqr_size)
                    col=int((pos[0] - self.config.board_lx) // self.config.sqr_size)
                    print(row,col)
                    if self.empty_cell(row,col):
                        self.add_go(self.player_current,row,col)
                        # self.draw_go(row,col)
                        print(self.cells)
                    
    def run_game(self):
        # Bucle principal del juego

        while not self.game_active:
            self.actualizar_ventana()
            self.revisar_eventos()
            self.clock.tick(60) #FPS
    
    
Tictactoe = Game()
Tictactoe.run_game()
