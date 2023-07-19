# Importar librerias
import pygame
import sys
from config import Configuraciones
from IA_logic import IA
from board import Board
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
        self.ai=IA()
        self.board=Board()
        self.cells=self.board.cells
        self.player_current= -1
        self.game_mode= "ai"
        self.game_over = False
        self.game_winner=False
        # Botones menu
        self.btn_pvp = pygame.Rect(415, 253, 330, 100)
        self.btn_pvc = pygame.Rect(415, 353, 330, 100)
        self.btn_conf = pygame.Rect(415, 453, 330, 100)
        # botones box question
        self.btn_vaj = pygame.Rect(365, 365, 200, 50)
        self.btn_vam = pygame.Rect(620, 365, 200, 50)
        
    def show_board(self):
        """Dibuja el tablero cuadriculado 3x3
        """
        # Dibujar fondo del tablero
        pygame.draw.rect(self.ventana,
                        (119, 136, 153),
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

    def draw_goes(self):
        """Dibuja las fichas de los jugadores
        """
        for r in range(3):
            for c in range(3):
                if self.board.cells[r][c] == -1:
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
                elif self.board.cells[r][c] == 1:
                    center = (self.config.circ_cr+c*self.config.sqr_size,self.config.circ_cc+r*self.config.sqr_size) 
                    pygame.draw.circle(
                        self.ventana, 
                        self.config.circ_color,
                        center,
                        self.config.circ_r,
                        self.config.circ_w
                    )
                    
    def change_turn(self):
        self.player_current = self.player_current *-1
    def ia_move(self):
        pygame.display.update()
        row,col = self.ai.eval(self.board)
        self.board.add_go(self.ai.player,row,col)
        self.change_turn()
    def state_game(self):
        return self.board.is_full_board() or self.board.final_state() != 0
    def show_winner_message(self):
        player_win = ("Jugador 1" if self.player_current == 1 else "Jugador 2")
        texto_show = "¡El ganador es el " + player_win + "!"
        if self.board.final_state()==0:
            texto_show = "Empate"
        font = pygame.font.SysFont(None, 48)
        text = font.render(texto_show, True, (255,255,255))
        text_rect = text.get_rect(center=(1200 // 2, 320))
        self.ventana.blit(text, text_rect)
    def checked_play_button(self,pos_mouse):
        """Inicia un nuevo juego cuando se hace click en algun boton."""
        if self.game_active == False:
            if self.btn_pvc.collidepoint(pos_mouse):
                self.game_active = True
                self.game_mode = "ai"
                self.ai.level=1
                print("modo ia")
                print(self.game_active)
            elif  self.btn_pvp.collidepoint(pos_mouse):
                print("modo pvp")
                self.game_active =True
                self.game_mode = "pvp"
                self.ai.level=0
                
        if self.game_active == "stop":
            
            if self.btn_vam.collidepoint(pos_mouse):
                print("volver al menu")
                self.game_active=False
                self.board.cells = [[0,0,0],[0,0,0],[0,0,0]]
                self.board.played=0
                self.player_current=-1
            elif  self.btn_vaj.collidepoint(pos_mouse):                
                print("volver a jugar")
                self.game_active=True
                self.board.cells = [[0,0,0],[0,0,0],[0,0,0]]
                self.board.played=0
                self.player_current=-1
    def actualizar_ventana(self):
        """Actualizar imagenes en la ventana y mostrar ventana actual."""
        
        self.ventana.blit(self.config.bg_menu,(0,0))
        # pygame.Rect(415, 353, 350, 200)
        # pygame.draw.rect(self.ventana,(0,0,0),(415, 353), 350, 200)
        # Redibuja el fondo del juego ACTIVO durante cada pasada por el bucle.
        if self.game_active:
            self.ventana.fill(self.config.bg_color)
            self.ventana.blit(self.config.bg_imagen,(0,0))
            self.show_board()
            self.draw_goes()
        
        if self.game_active == "stop":
            pygame.time.delay(200)
            self.ventana.blit(self.config.question_bx,(300,250))
            self.show_winner_message()
        #Actualizar pantalla
        pygame.display.flip()
    def revisar_eventos_mouse(self,pos):
        if self.game_active:
            row=int((pos[1] - self.config.board_ty)// self.config.sqr_size)
            col=int((pos[0] - self.config.board_lx) // self.config.sqr_size)
            print(row,col)
            if row in(0,1,2) and col in(0,1,2) and  self.board.empty_cell(row,col) and self.board.final_state()==0:
                self.board.add_go(self.player_current,row,col)
                self.change_turn()
                print(self.board.played)
        self.checked_play_button(pos)
                    
    def revisar_eventos(self):
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif evento.key == pygame.K_r:
                        self.game_active = False
                        self.board.cells = [[0,0,0],[0,0,0],[0,0,0]]
                        self.player_current=-1
                        self.board.played=0
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos=evento.pos
                    print(pos)
                    self.revisar_eventos_mouse(pos)
                    
    def run_game(self):
        # Bucle principal del juego

        while not self.game_over:
            self.actualizar_ventana()
            self.revisar_eventos()
            if (self.game_mode == "ai" and self.player_current == 1) and self.board.get_empty_cell()!=[]:
                self.ia_move()
            if self.state_game() and self.game_active:
                self.game_active = "stop"
                # print("PLAYER  WINNER:",-self.player_current)
                
            self.clock.tick(60) #FPS
            
    
    
Tictactoe = Game()
Tictactoe.run_game()
