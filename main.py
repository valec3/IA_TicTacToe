# Importar librerias
import pygame
import sys
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
        
        
    def actualizar_ventana(self):
        """Actualizar imagenes en la ventana y mostrar ventana actual."""
        # Redibuja el fondo durante cada pasada por el bucle.
        self.ventana.fill(self.config.bg_color)
        self.ventana.blit(self.config.bg_imagen,(0,0))
        
        self.show_board()
        
        #Actualizar pantalla
        pygame.display.flip()
        
    def revisar_eventos(self):
        pass
    def run_game(self):
        # Bucle principal del juego

        while not self.game_active:
            self.actualizar_ventana()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(60) #FPS
    
    
Tictactoe = Game()
Tictactoe.run_game()
