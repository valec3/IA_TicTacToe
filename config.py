import pygame

class Configuraciones:
    question_image_load=pygame.image.load('./img/box_question.png')
    bg_image_load = pygame.image.load('img/bg_ttt_active.jpg')
    bg_image_menu_load = pygame.image.load('img/bg_ttt_menu.jpg')
    def __init__(self) -> None:
        # Screen settings
        self.ventana_width = 1200
        self.ventana_height = 800
        self.bg_imagen=pygame.transform.scale(self.bg_image_load,(self.ventana_width,self.ventana_height))
        self.bg_menu = pygame.transform.scale(self.bg_image_menu_load,(self.ventana_width,self.ventana_height))
        self.question_bx= pygame.transform.scale(self.question_image_load,(600,280))
        self.bg_color=(255,255,255)
        
        # Caracteristicas Tablero
        self.sqr_size=self.ventana_height//4
        self.board_sz_w=self.sqr_size*3
        self.board_lx=(self.ventana_width-self.board_sz_w)/2    #limite izquierdo del tablero
        self.board_dx=self.board_lx+self.board_sz_w             #limite derecho del tablero
        self.board_ty=(self.ventana_height-self.board_sz_w)/2   #limite superior del tablero
        self.board_by=self.board_ty + self.board_sz_w           #limite inferior del tablero
        self.board_color=(0,0,0)
        # 1200 - 900 = 300 / 2 
        
        # Configuraciones Jugador 2 (circulo)
        self.circ_w = 15
        self.circ_r = self.sqr_size//3     
        self.circ_cr = self.board_lx + self.sqr_size//2    #eje x del centro del circulo
        self.circ_cc = self.board_ty + self.sqr_size//2    #eje y del centro del circulo
        self.circ_color = (0, 255, 255) 
        
        self.cross_color = (0,0,0)
        self.cross_lls = 35 + self.board_lx
        self.cross_lle = 35 + self.board_ty
        self.cross_w = 25

config = Configuraciones()

